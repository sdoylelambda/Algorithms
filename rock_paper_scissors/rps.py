#!/usr/bin/python

import sys

def rock_paper_scissors(number_of_plays):
  all_moves = []
  move_options = ['rock', 'paper', 'scissors']

  def build_moves(countdown, piece_being_built):
    if countdown == 0:
      all_moves.append(piece_being_built)
      return

    for move in move_options:
      new_piece_result = piece_being_built + [move]
      build_moves(countdown -1, new_piece_result)
  build_moves(number_of_plays, [])

  return all_moves

print(rock_paper_scissors(2))













if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')