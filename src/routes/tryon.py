import os
import sys
import torch
import base64
import io
from PIL import Image
from flask import Blueprint, request, jsonify
import numpy as np

# Add tryondiffusion to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'tryondiffusion'))

# Import tryondiffusion modules exactly as they are
from tryondiffusion import TryOnImagen, get_unet_by_name

tryon_bp = Blueprint('tryon', __name__)

# Global variables to store the model (loaded once)
imagen_model = None
device = None

def initialize_model():
    """Initialize the TryOnDiffusion model exactly as in the repository examples"""
    global imagen_model, device
    
    if imagen_model is not None:
        return imagen_model, device
    
    # Use the exact code from the repository examples
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # Get UNets exactly as in the repository
    unet1 = get_unet_by_name("base")
    unet2 = get_unet_by_name("sr")
    
    # Create TryOnImagen exactly as in the repository
    imagen_model = TryOnImagen(
        unets=(unet1, unet2),
        image_sizes=((128, 128), (256, 256)),
        timesteps=(256, 128),
    )
    imagen_model = imagen_model.to(device)
    
    return imagen_model, device

def preprocess_image(image_data, target_size=(256, 256)):
    """Preprocess image for the model"""
    # Decode base64 image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to target size
    image = image.resize(target_size, Image.Resampling.LANCZOS)
    
    # Convert to tensor exactly as expected by the model
    image_array = np.array(image).astype(np.float32) / 255.0
    image_tensor = torch.from_numpy(image_array).permute(2, 0, 1).unsqueeze(0)
    
    return image_tensor

def create_dummy_poses(batch_size=1):
    """Create dummy pose data as required by the model"""
    # The model expects pose data with shape (batch_size, 18, 2)
    # This is a simplified version - in real usage, you'd extract actual poses
    dummy_poses = torch.randn(batch_size, 18, 2)
    return dummy_poses

@tryon_bp.route('/tryon', methods=['POST'])
def tryon():
    """Virtual try-on endpoint using tryondiffusion repository code as-is"""
    try:
        # Get request data
        data = request.json
        if not data or 'person_image' not in data or 'garment_image' not in data:
            return jsonify({'error': 'Missing person_image or garment_image'}), 400
        
        # Initialize model
        imagen, device = initialize_model()
        
        # Preprocess images
        person_image_b64 = data['person_image'].split(',')[1] if ',' in data['person_image'] else data['person_image']
        garment_image_b64 = data['garment_image'].split(',')[1] if ',' in data['garment_image'] else data['garment_image']
        
        # Process images exactly as the model expects
        ca_images = preprocess_image(person_image_b64, (256, 256)).to(device)
        garment_images = preprocess_image(garment_image_b64, (256, 256)).to(device)
        
        # Create pose data (simplified - in real usage you'd extract actual poses)
        person_poses = create_dummy_poses(1).to(device)
        garment_poses = create_dummy_poses(1).to(device)
        
        # Generate try-on result using the exact repository code
        with torch.no_grad():
            images = imagen.sample(
                ca_images=ca_images,
                garment_images=garment_images,
                person_poses=person_poses,
                garment_poses=garment_poses,
                batch_size=1,
                cond_scale=2.0,
                start_at_unet_number=1,
                return_all_unet_outputs=False,
                return_pil_images=True,
                use_tqdm=True,
                use_one_unet_in_gpu=True,
            )
        
        # Convert result to base64
        if images and len(images) > 0:
            result_image = images[0]
            
            # Convert PIL image to base64
            buffered = io.BytesIO()
            result_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            return jsonify({
                'success': True,
                'result_image': f"data:image/png;base64,{img_str}",
                'message': 'Try-on generated successfully using TryOnDiffusion'
            })
        else:
            return jsonify({'error': 'Failed to generate try-on result'}), 500
            
    except Exception as e:
        print(f"Error in tryon endpoint: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@tryon_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return jsonify({
            'status': 'healthy',
            'device': device,
            'model_loaded': imagen_model is not None,
            'message': 'TryOnDiffusion Flask API is running'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

