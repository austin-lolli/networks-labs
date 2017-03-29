def demultiplex(input_file):
        msgs = [[], [], [], [], []]
        with open(input_file, 'r') as f:
                for line in f:
                        m = ""
                        l = line.split()
                        for i in range(1, len(l)):
                                m += (l[i] + " ")
                        if m == "No messages ":
                                continue
                        elif l[0] == "60400:":
                                msgs[0].append(m)
                        elif l[0] == "60401:":
                                msgs[1].append(m)
                        elif l[0] == "60402:":
                                msgs[2].append(m)
                        elif l[0] == "60403:":
                                msgs[3].append(m)
                        else:
                                msgs[4].append(m)
                print(msgs)
                print(len(msgs[4]))

demultiplex("muxed_stream")
