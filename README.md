# Deep Transient 

This repository contains the model files, solver definitions, and
learned weights for the networks described in the following
publication: 

> A Fast Method for Estimating Transient Scene Attributes (Ryan
> Baltenberger, Menghua Zhai, Connor Greenwell, Scott Workman, 
> Nathan Jacobs), In IEEE Winter Conference on Applications of
> Computer Vision (WACV), 2016.
> [pdf](http://cs.uky.edu/~rbalten/transient/docs/Baltenberger_Transient-Attributes_WACV16.pdf) 

```
@article{baltenberger16transient,
  title = {{A Fast Method for Estimating Transient Scene Attributes}}, 
  author = {Baltenberger, Ryan and Zhai, Menghua and Greenwell, Connor and Workman, Scott and Jacobs, Nathan}, 
  journal = {{IEEE Winter Conference on Applications of Computer Vision (WACV)}}, 
  year = {2016}, 
  volume = {2016}, 
  number = {1}, 
  pages = {8}
}
```

## Getting Started

Download the model weights:

```
./download_models.sh
```

Run the example:

```
python example.py
```

To suppress Caffe output while running:

```
python example.py 2>/dev/null
```

## License

This software is released under a creative commons license which
allows for personal and research use only. For a commercial license
please contact the authors. You can view a license summary here:
http://creativecommons.org/licenses/by-nc/4.0/

## Contact

Ryan Baltenberger  
University of Kentucky  
http://cs.uky.edu/~rbalten/


