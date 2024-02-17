def solution(participant, completion):
    answer = ''
    nparticipant = sorted(participant)
    ncompletion = sorted(completion)
    for i, part in enumerate(nparticipant):
        if i >= len(completion):            
            return nparticipant[i]
        else:
            
            if part != ncompletion[i]:
                return nparticipant[i]