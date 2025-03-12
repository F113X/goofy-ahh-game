chmod +x goofyahhgame.py
mv goofyahhgame.py goofyahh
mkdir -p ~/bin
cp -av goofyahh ~/bin

echo 'export PATH=$PATH":$HOME/bin"' >> Users/YOURHOMEDIR/.zprofile

source Users/YOURHOMEDIR/.zprofile