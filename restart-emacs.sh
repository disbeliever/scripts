#!/bin/sh

emacsclient -e "(kill-emacs)"
emacs --daemon --chdir $HOME
