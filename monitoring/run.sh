#prepare environment
ssh root@worker1 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit
eof

ssh root@worker2 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit
eof

ssh root@worker3 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit
eof

ssh root@worker4 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit

eof
ssh root@worker5 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit
eof
ssh root@worker6 << eof
yum install -y  python-devel wget 
if [ ! -f "/tmp/get-pip.py" ]; then
	wget https://bootstrap.pypa.io/get-pip.py -P /tmp
fi
if [ -f "/tmp/monitor_cpu.txt" ]; then
	rm /tmp/monitor_cpu.txt
fi
if [ -f "/tmp/monitor_mem.txt" ]; then
	rm /tmp/monitor_mem.txt
fi
if [ -f "/tmp/monitor_IO.txt" ]; then
	rm /tmp/monitor_IO.txt
fi
if [ -f "/tmp/monitor_net.txt" ]; then
	rm /tmp/monitor_net.txt
fi
python /tmp/get-pip.py
pip install colorama
exit
eof

# copy python files to hosts
echo "copying to worker1..."
scp monitorS.py scidb@worker1:/tmp
echo "copying to worker2..."
scp monitorS.py scidb@worker2:/tmp
echo "copying to worker3..."
scp monitorS.py scidb@worker3:/tmp
echo "copying to worker4..."
scp monitorS.py scidb@worker4:/tmp
echo "copying to worker5..."
scp monitorS.py scidb@worker5:/tmp
echo "copying to worker6..."
scp monitorS.py scidb@worker6:/tmp

# run main program
python monitorM.py

# free memory
#echo 1 > /proc/sys/vm/drop_caches

echo "Done"
