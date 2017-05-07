#!/bin/bash
#
# Download text models.

cd "$(dirname "$0")"

die() {
  echo >&2 $*
  exit 1
}

checkCmd() {
  command -v $1 >/dev/null 2>&1 \
    || die "'$1' command not found. Please install from your package manager."
}

checkCmd wget

if [ ! -f data/text.model ]; then
  printf "\n\n====================================================\n"
  printf "Downloading text.model.\n"
  printf "This will incur about 5MB of network traffic\n"
  printf "====================================================\n\n"
  wget \
       http://silenceender.com/files/text.model \
       -O data/text.model
  [ $? -eq 0 ] || die "+ Error in wget."
fi

if [ ! -f data/text.model.syn1neg.npy ]; then
  printf "\n\n====================================================\n"
  printf "Downloading text.model.syn1neg.npy\n"
  printf "This will incur about 57MB of network traffic for the models.\n"
  printf "====================================================\n\n"

  wget \
       http://silenceender.com/files/text.model.syn1neg.npy \
       -O data/text.model.syn1neg.npy
  [ $? -eq 0 ] || ( rm data/text.model.syn1neg.npy* && die "Error in wget." )

fi

if [ ! -f data/text.model.wv.syn0.npy ]; then
  printf "\n\n====================================================\n"
  printf "Downloading text.model.wv.syn0.npy\n"
  printf "This will incur about 57MB of network traffic for the models.\n"
  printf "====================================================\n\n"

  wget \
       http://silenceender.com/files/text.model.wv.syn0.npy \
       -O data/text.model.wv.syn0.npy
  [ $? -eq 0 ] || ( rm data/text.model.wv.syn0.npy* && die "Error in wget." )

fi

printf "\n\n====================================================\n"
printf "Verifying checksums.\n"
printf "====================================================\n\n"

md5str() {
  local FNAME=$1
  case $(uname) in
    "Linux")
      echo $(md5sum "$FNAME" | cut -d ' ' -f 1)
      ;;
    "Darwin")
      echo $(md5 -q "$FNAME")
      ;;
  esac
}

checkmd5() {
  local FNAME=$1
  local EXPECTED=$2
  local ACTUAL=$(md5str "$FNAME")
  if [ $EXPECTED = $ACTUAL ]; then
    printf "+ $FNAME: successfully checked\n"
  else
    printf "+ ERROR! $FNAME md5sum did not match.\n"
    printf "  + Expected: $EXPECTED\n"
    printf "  + Actual: $ACTUAL\n"
    printf "  + Please manually delete this file and try re-running this script.\n"
    return -1
  fi
  printf "\n"
}

set -e

checkmd5 \
  data/text.model \
  848f28ae47f551e0b2c7b59a5dc14d0b

checkmd5 \
  data/text.model.syn1neg.npy \
  0be602d9ed09be22fe6e03ca23909002

checkmd5 \
  data/text.model.wv.syn0.npy \
  53a33bbc06d0c8d5a91be52605ca8758
