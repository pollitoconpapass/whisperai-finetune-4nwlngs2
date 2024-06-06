# WHISPER-AI FINE TUNING (4NwLngs2)

Notebook for finetuning Whisper-small model with supported and new languages.  

4NwLngs2 -> 'For New Languages Too'

### REQUIREMENTS
You'll need a Hugging Face dataset with Audios and its respective transcription. Something like [this dataset](https://huggingface.co/datasets/pollitoconpapass/test-genesis-quzbible-v4) which is in Quechua language. (Is just a test for this model)


If you want to know how to build it, check this [other repo](https://github.com/pollitoconpapass/TTS-Audio-Dataset-Creation). 

### SOME GUIDANCE
- `api.py` is just a test file for creating an API from your Finetuned model.
- `fine_tuning.ipynb` is the Jupyter Notebook you're gonna be using for the finetuning.
- `preprocessor_config.json` is the json file needed to work correctly. Is uploaded in case this process didn't create one in your HuggingFace repo.
- `requirements.txt` you may need to install it when using the `api.py`
