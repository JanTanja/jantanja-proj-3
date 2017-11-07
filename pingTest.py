from TestSim import TestSim

def main():
    # Get simulation ready to run.
    s = TestSim();

    # Before we do anything, lets simulate the network off.
    s.runTime(1);

    # Load the the layout of the network.
    s.loadTopo("long_line.topo");

    # Add a noise model to all of the motes.
    s.loadNoise("no_noise.txt");

    # Turn on all of the sensors.
    s.bootAll();

    # Add the main channels. These channels are declared in includes/channels.h
    s.addChannel(s.COMMAND_CHANNEL);
    s.addChannel(s.GENERAL_CHANNEL);
    s.addChannel(s.FLOODING_CHANNEL);
    s.addChannel(s.NEIGHBOR_CHANNEL);
    s.addChannel(s.ROUTING_CHANNEL);
    s.addChannel(s.TRANSPORT_CHANNEL);

    s.runTime(300);
    s.testServer(1);
    s.runTime(60);

    s.ping(9,1, "hello alex\r\n");
    s.runTime(500);

    s.chat(6,"hello dan\r\n");
    s.runTime(800);

    s.chat(9,"hello ashley\r\n");
    s.runTime(800);

    s.chat(3,"listusers\r\n");
    s.runTime(800);

    s.chat(9,"message hi guys\r\n");
    s.runTime(900);

    #s.neighborDMP(3);

    #s.ping(9, 1, "Hi!");
    #s.runTime(30);
    #s.neighborDMP(3);
    #s.runTime(15);
    #s.moteOff(6);
    #s.runTime(1);
if __name__ == '__main__':
    main()
