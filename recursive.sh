#!/bin/bash
factorial() {
  if (($1 < 1)); then
    echo 1
  else
    last=$(factorial $(($1 - 1)))
    x=$(($1 * last))
    echo $x
    return

  fi
}

factorial 10
