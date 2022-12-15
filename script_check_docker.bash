set -o posix

substring = "docker-ce"
substring2 = "docker-compose"
substring3 = "docker-ce-cli"
substring4 = "containerd.io"
salida= apt list --installed | grep docker

if [[ $salida = $substring* ]]; then
    echo "docker-ce is installed!"
else
    echo "We going to install docker-ce"
    apt-get update && apt-get install docker-ce -y
fi
################# 2
if [[ $salida = $substring2* ]]; then
    echo "docker-compose is installed!"
else
    echo "We going to install docker-compose"
   apt-get update && apt-get install docker-compose -y
fi
################# 3
if [[ $salida = $substring3* ]]; then
    echo "docker-ce-cli is installed!"
else
    echo "We going to install docker-ce-cli"
    apt-get update && apt-get install docker-ce-cli -y
fi
################# 4
if [[ $salida = $substring4* ]]; then
    echo "containerd.io is installed!"
else
    echo "We going to install containerd.io"
    apt-get update && apt-get install containerd.io -y
fi
#apt install docker-ce docker-compose docker-ce-cli containerd.io
echo "Checking again the docker packages installed..."
echo "You should see this packages installed: docker-ce docker-compose docker-ce-cli containerd.io"
salida= apt list --installed | grep docker
echo "If this script fail, consider run manually for Ubuntu/Debian:"
echo "apt install docker-ce docker-compose docker-ce-cli containerd.io -y"
echo "Or, for Alpine: apk add docker-ce docker-compose docker-ce-cli containerd.io"
exit 1
