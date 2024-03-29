# 5x5 Alpha Zero Go
Neural Network to play the game of Go

# Credits
Original project by Surag Nair<br>
<a href="https://github.com/suragnair/alpha-zero-general">Alpha Zero General</a>

# How to train it?
Just run **python train.py**, it would complete a single cycle
of training. You can then continue training with the existing
model.

# How to change board size
You can simply change the arg to Game() to a desired size,
beware though, training on larger board takes much longer
and also NN arch might need to get improved as well as
some additional changes to game logic and scoring.

# How to use it?
You can play vs the model you've trained yourself or <a href="https://github.com/maksimKorzh/go-nn/releases/tag/0.1">download</a>
pre-trained models from the releases. Adjust path to NN model
in **play-nn.py** or **play-old-vs-new.py** and play vs the
network yourself or watch it playing itself or other models

# Watch how it works
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/5UYA-V2a3cc/0.jpg)](https://www.youtube.com/watch?v=5UYA-V2a3cc&list=PLmN0neTso3JyAmv7LWhA8GBGUWoxXoysa)
