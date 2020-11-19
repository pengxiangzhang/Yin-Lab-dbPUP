def blastp(query):
    with open('pup_blastp/search.fsa', 'w') as f:
        f.writelines(query)
    command = "./blast/blastp -db pup_blastp/PUP_db -query pup_blastp/search.fsa -out pup_blastp/results.blast -outfmt 6 -evalue 1e-5 -num_threads 2"
    # command = "./blast/blastp -db pup_blastp/PUP_db -query " + query + " -out pup_blastp/results.blast -outfmt 6 -evalue 1e-5 -num_threads 4"
    os.system(command)

    with open('pup_blastp/results.blast', 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            return []

    data = pd.read_csv('pup_blastp/results.blast', sep="\t", header=None)
    index = 0
    processed_blastp = []
    for unid in data[1]:
        char_record = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
        swis_record = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
        trem_record = treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
        if char_record != None:
            char_result = []
            char_result.append(data[0][index])
            char_result.append(unid)
            char_result.append(char_record.family)
            char_result.append(data[2][index])
            char_result.append(data[10][index])
            char_result.append(char_record.protein_name)
            char_result.append(char_record.strain)
            char_result.append("")
            processed_blastp.append(char_result)
        if swis_record != None:
            swis_result = []
            swis_result.append(data[0][index])
            swis_result.append(unid)
            swis_result.append(swis_record.family)
            swis_result.append(data[2][index])
            swis_result.append(data[10][index])
            swis_result.append(swis_record.protein_enzyme)
            swis_result.append(swis_record.strain)
            swis_result.append(swis_record.web_id)
            processed_blastp.append(swis_result)
        if trem_record != None:
            trem_result = []
            trem_result.append(data[0][index])
            trem_result.append(unid)
            trem_result.append(trem_record.family)
            trem_result.append(data[2][index])
            trem_result.append(data[10][index])
            trem_result.append(trem_record.protein_enzyme)
            trem_result.append(trem_record.strain)
            trem_result.append(trem_record.web_id)
            processed_blastp.append(trem_result)

        index += 1
    # for item in processed_blastp:
    #     print(item)
    return processed_blastp