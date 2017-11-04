speed = 76660813  # ∆ Put your answer here.
hero.say(speed)

#************************************************************************
# Say the correct speed to insert our spybot into the line of robots.
# We must find the exact speed in robot motor revolutions per month.
# We've found the part of the robot code that controls the speed,
# but we don't know how to interpret it to find the final speed.
# What's the value of %eax when the last instruction (the NOP) runs?

#speed = 0  # ∆ Put your answer here.
#hero.say(speed)

# Check the Help (File tab) to see the file. It's also included below.
# ------------------------------------------
# # This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# # and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
# # AT&T syntax by default.
# MOV $8156,%ebx
# MOV $9400,%eax
# MOV $14987,%ecx
# CMP %eax,%ebx
# JL L1
# JMP L2
# L1:
# IMUL %eax,%ebx
# ADD %eax,%ebx
# MOV %ebx,%eax
# SUB %ecx,%eax
# JMP L3
# L2:
# IMUL %eax,%ebx
# SUB %eax,%ebx
# MOV %ebx,%eax
# ADD %ecx,%eax
# L3:
# NOP
