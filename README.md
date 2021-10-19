# tfite model maker kütüphanesi ile nesne tespiti

<p align="center">
  <img src="https://raw.githubusercontent.com/mecitsezginn/object_detection_with_tflite_model_maker/main/img.jpg" width="750" title="hover text">
</p>

## Kütüphane kurulumu
- pip install tflite-model-maker
- pip install pycocotools
- pip install tensorflow==2.5

### * dipnot
tflite model maker kütüphanesi kurulurken tensorflow 2.6 sürümünü de kurmaktadır. tflite dosyasına dönüşüm yapıldığında 2.5 ve 2.6 arasında 
output farkı bulunmaktadır. Bu nedenle tensorflow 2.5 sürümü kullanılması tavsiye ederim.

### * dipnot2
tflite dosyası default olarak 25 çıktı veriyor. Çıktı sayısını değiştirmek için;
```
from tflite_model_maker.object_detector import EfficientDetSpec
```
"EfficientDetSpec" üzerine crtl + mouse left yaptığımızda 
"C:/ProgramData/Anaconda3/lib/site-packages/tensorflow_examples/lite/model_maker/core/task/model_spec/object_detector_spec.py" 
dosyasına yönlendirecek.

```
class EfficientDetModelSpec(object):
  """A specification of the EfficientDet model."""

  compat_tf_versions = compat.get_compat_tf_versions(2)

  def __init__(self,
               model_name: str,
               uri: str,
               hparams: str = '',
               model_dir: Optional[str] = None,
               epochs: int = 50,
               batch_size: int = 64,
               steps_per_execution: int = 1,
               moving_average_decay: int = 0,
               var_freeze_expr: str = '(efficientnet|fpn_cells|resample_p6)',
               tflite_max_detections: int = 25,
               strategy: Optional[str] = None,
               tpu: Optional[str] = None,
               gcp_project: Optional[str] = None,
               tpu_zone: Optional[str] = None,
               use_xla: bool = False,
               profile: bool = False,
               debug: bool = False,
               tf_random_seed: int = 111111,
               verbose: int = 0) -> None:
```

```
tflite_max_detections: int = 10,
```
değerini değiştirerek model çıktı sayısını değiştirebiliriz.

## Fotoğrafları etiketleme
[Labelimg](https://github.com/tzutalin/labelImg) kullanarak xml dosyaları oluşturabiliriz.


## Kaynaklar
https://www.tensorflow.org/lite/tutorials/model_maker_object_detection

https://gilberttanner.com/blog/tflite-model-maker-object-detection
