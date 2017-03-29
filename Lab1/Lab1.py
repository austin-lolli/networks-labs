#python3
#!/usr/bin/python
# Lab 1 Multiplexing Lab 
# Austin Lolli 1/20/17
# Written for Python 3 and tested in 3.6.0

import sys


def multiplex(stream):
    count = 0	# Number of messages written to file		
    with open('muxed_stream', 'w') as f:
# This for loop finds the longest incoming message and saves it.
# It s then saved for use in the range on multiplexing loop. 
        x = len(stream[0])
        for a in range(len(stream)):
            if len(stream[a]) > x:
                x = len(stream[a])
        x = x//5 + 1	# Number of times to cycle through messages
# This part of the function goes through the list of machines x number of times (the 
# upper bound of the longest message divided by 5), and then for each machine, writes  
# 5 messages. If the current machine has no messages to write, it writes No messages and
# breaks. By breaking when there is no messages to write, the function becomes Statistical 
# Time Division Multiplexing, since the machine with no messages doesn't send blanks for
# redundant ticks. We determine whether a machine has a message to write by using a try 
# and except IndexError. First, try to pop the message from the machines stream, if there 
# is a message, it is stored and written to file, and the message count is incrimented. An
# index error means the machines message list is empty, and therefore writes no message,
# and lastly breaks to move on to the next machine. 
        for i in range(0, x):
            for j in range(0, len(stream)): 
                for k in range(0, 5):
                    try:
                        msg = stream[j].pop(0)
                        f.write("6040{}: {} \n".format(j, msg))
                        count += 1
                    except IndexError:		
                        f.write("6040{}: No messages \n".format(j))
                        break					

        return count


def demultiplex(input_file):
    msgs = [[], [], [], [], []]	# List of lists for all incoming messages
    with open(input_file, 'r') as f:
        for line in f:
            m = ""			# Empty message variable
            l = line.split() 	# Stores the entire line as a list, l. 
# This for loop takes every member of l, omitting the first (the machine ID) 
# and appends it to m with a space (line.split doesnt record spaces). At end 
# of the for loop, m containts the entire message for this machine tick.
# After m has message stored, check l[0] to determine what machine sent message
# and store it to the corresponding list. 
            for i in range(1, len(l)):
                m += (l[i] + " ")
            if m == "No messages ": 
                continue	# No message, nothing to write/append, move to next file line. 	
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
	
    return tuple(msgs)

## YOU DON'T NEED TO EDIT ANYTHING BELOW HERE

def test_case_1():
    """Testing Multiplexing with tons of messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ('1', '2', '3', '4', '5', '6', '7', '8', '9'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'),
        ('1', '2', '3', '4'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 9
    assert len(messages_received[1]) == 17
    assert len(messages_received[2]) == 20
    assert len(messages_received[3]) == 16
    assert len(messages_received[4]) == 24

def test_case_2():
    """Testing multiplexing with tons of lost messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ("This ain't", "no intro,", " this the entree"),
        (),
        (),
        (),
        ("Hit that", "intro with Kanye ", "and sound like Andre"),
        ("Tryna", "turn", "my", "baby", "mama", "to", "my", "fiancee"),
        ("She like"," music, she from", "Houston",  "like Auntie Yonce"),
        ("Man my daughter couldn't", "have a better mother"),
        ("If she ever", "find another, he", "better", "love", "her")
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 3
    assert len(messages_received[1]) == 0
    assert len(messages_received[2]) == 0
    assert len(messages_received[3]) == 0
    assert len(messages_received[4]) == 22


if __name__ == '__main__':
    test_case_1()
    test_case_2()

