import numpy as np

"""Constants to be used for our poker hands""" 

# Ranks are column vectors
ranks = {
  'ace'   : np.matrix('1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0'),
  'two'   : np.matrix('0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0'),
  'three' : np.matrix('0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0'),
  'four'  : np.matrix('0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0'),
  'five'  : np.matrix('0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0'),
  'six'   : np.matrix('0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0'),
  'seven' : np.matrix('0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0'),
  'eight' : np.matrix('0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0'),
  'nine'  : np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0'),
  'ten'   : np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0'),
  'jack'  : np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0'),
  'queen' : np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0'),
  'king'  : np.matrix('0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1')
}

# Suits are row vectors
suits = {
  'clubs'    : np.matrix('1 0 0 0'),
  'diamonds' : np.matrix('0 1 0 0'),
  'hearts'   : np.matrix('0 0 1 0'),
  'spades'   : np.matrix('0 0 0 1')
}
