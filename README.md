# Train RL agents to play Pokemon Red

A fork of [Pokemon Red Experiments](https://github.com/PWhiddy/PokemonRedExperiments) designed to augment the reinforcement learning model with additional state context derived from a YOLO object recognition model. Please check out the original repo and youtube video, it is very cool!

NOTE: This project has been developed and run solely on ubuntu with NVIDIA hardware. Other operating systems and hardware may or may not work, you are welcome to try but no support will be provided.

## Running the Pretrained Model Interactively 🎮  
🐍 Python 3.12 is recommended. Other versions may work but have not been tested.
You also need to install ffmpeg and have it available in the command line.

### Reinforcemment Model Setup

1. Copy your legally obtained Pokemon Red ROM into the base directory. You can find this using google, it should be 1MB. Rename it to `PokemonRed.gb` if it is not already. The sha1 sum should be `ea9bcae617fdf159b045185467ae58b2e4a48b9a`, which you can verify by running `shasum PokemonRed.gb`. 
2. Move into the base directory (the parent directory of this repo alongside the README.md)
3. Install the src dependencies:

```cd src```  
Create a new conda environment to isolate the dependencies:
```
conda create -n pokemon_with_vision python=3.12
```

Activate the conda environment
```
conda activate pokemon_with_vision
```
Install the dependencies in your new environment
```pip install -r requirements.txt```
It may be necessary in some cases to separately install the SDL libraries.

__NOTE:__ If you have a 50 series GPU (eg 5070, 5080, etc.), the current stable pytorch builds do not support these GPUs yet. After installing the requirements you will need to additionally run:

```
pip install torch==2.7.1+cu128 --extra-index-url https://download.pytorch.org/whl/cu128
```

4. Fetch the utralytics YOLO11s model weights

```wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt```

5. Run:  
```python run_pretrained_interactive.py```
  
Interact with the emulator using the arrow keys and the `a` and `s` keys (A and B buttons).  
You can pause the AI's input during the game by editing `agent_enabled.txt`

Note: the Pokemon.gb file MUST be in the main directory and your current directory MUST be the `src/` directory in order for this to work.

## Vision Model Setup

The vision model is trained on the following dataset

https://universe.roboflow.com/pokemonfireredleafgreenv0/dataset_pokemon_firered_leafgreen_v0/dataset/1

^ As the sprites in the dataset are sourced from Gameboy Advanced games, the images were transformed to greyscale to improve adaptability to recognise images in original gameboy games. In the future to improve results a pure Gameboy-sprite image dataset may be generated.

1. Download the dataset as a zip in yolov11 form 

2. Extract the zip and copy the dataset_v0.v1i.yolov11 directory into src/vision_model/

## Training the Reinforcement Learning Model 🏋️ 

<img src="/assets/grid.png?raw=true" height="156">


### src

- Trains faster and with less memory
- Reaches Cerulean
- Streams to map by default
- Other improvements

Replaces the frame KNN with a coordinate based exploration reward, as well as some other tweaks.
1. Previous steps but in the `src` directory instead of `src`
2. Run:
```python baseline_fast_src.py```

## Tracking Training Progress 📈

### Training Broadcast
Stream your training session to a shared global game map using the [Broadcast Wrapper](/src/stream_agent_wrapper.py) on your environment like this:
```python
env = StreamWrapper(
            env, 
            stream_metadata = { # All of this is part is optional
                "user": "super-cool-user", # choose your own username
                "env_id": id, # environment identifier
                "color": "#0033ff", # choose your color :)
                "extra": "", # any extra text you put here will be displayed
            }
        )
```

Hack on the broadcast viewing client or set up your own local stream with this repo:  
  
https://github.com/pwhiddy/pokerl-map-viz/

### Local Metrics
The current state of each game is rendered to images in the session directory.   
You can track the progress in tensorboard by moving into the session directory and running:  
```tensorboard --logdir .```  
You can then navigate to `localhost:6006` in your browser to view metrics.  
To enable wandb integration, change `use_wandb_logging` in the training script to `True`.

## Static Visualization 🐜
Map visualization code can be found in `visualization/` directory.

## Supporting Libraries
Check out these awesome projects!
### [PyBoy](https://github.com/Baekalfen/PyBoy)
<a href="https://github.com/Baekalfen/PyBoy">
  <img src="/assets/pyboy.svg" height="64">
</a>

### [Stable src 3](https://github.com/DLR-RM/stable-src3)
<a href="https://github.com/DLR-RM/stable-src3">
  <img src="/assets/sblogo.png" height="64">
</a>
