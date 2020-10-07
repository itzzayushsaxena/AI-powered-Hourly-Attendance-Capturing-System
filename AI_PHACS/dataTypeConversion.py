def tupleToList(tuple):
    subjectid_list = []
    for i in range(0, len(tuple)):
        subjectid_list.append(tuple[i][0])
    return subjectid_list