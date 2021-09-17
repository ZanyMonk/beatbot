# BeatBot - audio streaming Discord bot

## Introduction
Beatbot is a self-hostable, single-server, home-made audio streaming bot that can
take input from YouTube, SoundCloud and virtually every platform `youtube-dl` supports.

## Getting started
### Docker
```shell
git clone https://github.com/ZanyMonk/docker-beatbot beatbot
cd beatbot
docker-compose up
```

### Boomer
```shell
git clone https://github.com/ZanyMonk/beatbot
cd beatbot
pip install -r requirement.txt
./beatbot.py
```


## @TODO
- [ ] Fix vocal channel management
  - [ ] Quit all vocal channels when exiting
  - [ ] Auto-select a vocal channel when instigator isn't connected to any
  - [ ] Stabilize hard-reboot
- [ ] Rebase Docker image on `python:3.7-alpine`
- [ ] Finish reaction-based control
  - [ ] Implement button-like reactions
  - [ ] Improve embed filter for initial reaction (slash-command ?)
- [ ] Implement slash-command controls