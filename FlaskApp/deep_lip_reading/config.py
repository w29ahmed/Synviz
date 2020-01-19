import configargparse


# Define config class to use instead of parser
class Config:
  def __init__(self):
    self.gpu_id = ''
    
    self.print_predictions = False
    self.seed = 0
    self.tb_eval = False

    self.data_path = 'deep_lip_reading/media/example'
    self.data_list = 'deep_lip_reading/media/example/demo_list.txt'

    self.batch_size = 1

    self.img_width = 160
    self.img_height = 160
    self.img_channels = 1
    self.n_labels = 45
    self.pad_mode = 'mid'

    self.time_dim = 145
    self.maxlen = 145
    self.transcribe_digits = False

    self.lip_model_path = 'deep_lip_reading/models/lrs2_lip_model'

    self.graph_type = 'infer'
    self.net_input_size = 112
    self.featurizer = True
    self.feat_dim = 512

    self.num_blocks = 6
    self.hidden_units = 512
    self.num_heads = 8
    self.dropout_rate = 0.1
    self.sinusoid = True
    self.mask_pads = False

    self.lm_path = 'deep_lip_reading/models/lrs2_language_model'
    self.beam_size = 4
    self.len_alpha = 0.7
    self.lm_alpha = 0.05
    self.top_beams = 1

    self.resize_input = 160
    self.scale = 1.4
    self.mean = 0.4161
    self.std = 0.1688

    self.horizontal_flip = False
    self.crop_pixels = 0
    self.test_aug_times = 0
    self.n_eval_times = 1 


def load_args(default_config=None):
  return Config()
