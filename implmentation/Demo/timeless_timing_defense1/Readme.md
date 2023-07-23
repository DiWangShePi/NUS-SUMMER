# Demo of Timeless Timing Attack Defense

## Introduction
This is a demo of timeless timing attack defense.We use random time delay to ensure that the secret can not be guessed.

## Build
1.Victim server

`docker-compose build up -d`

2.Attacker

`docker build -t timeless_attack -f Dockerfile.exploit .
`
## Attack
`
docker run -it --rm --network=host -e TARGET='http://localhost:9994' timeless_attack
`

## Result

Now due to the random delay,  we can't guess the secret on the server properly.