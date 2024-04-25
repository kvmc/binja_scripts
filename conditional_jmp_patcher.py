def get_conditional_jumps():
    entries = {} 
    counter = 0
    cnd_jmps = ['jz','je','jnz','jne','jc','jnc','jo','jno','js','jns','jp','jpe','jnp','jpo']
    for i in bv.instructions:
        if i[0][0].text in cnd_jmps:
            entries.update({counter:i})
            counter += 1
    return entries

def fix_conditional_jumps(jmp_list):
    for i in range(len(jmp_list)-1):
        currinst,currinstlen = jmp_list[i][1]
        currinstlen = bv.get_instruction_length(jmp_list[i][1])
        nextinst = jmp_list[i+1][1]

        if  (currinst+currinstlen == nextinst) and (jmp_list[i][0][2] == jmp_list[i+1][0][2]):
            target = jmp_list[0][2]	
            print(f"Patching @ {jmp_list[i][1]}") 
            print(f"Match 1: {jmp_list[i][1]} -> {jmp_list[i][0]}")
            print(f"Match 2: {jmp_list[i+1][1]} -> {jmp_list[i+1][0]}")
            target = jmp_list[i][0][2]
            instlen = bv.get_instruction_length(jmp_list[i][1]) + bv.get_instruction_length(jmp_list[i+1][1])

            for j in range(instlen):
                bv.write(jmp_list[i][1]+i,bv.arch.assemble('int3'))

            bv.write(jmp_list[i][1],bv.arch.assemble(f'jmp {target}'))




bv.update_analysis()
