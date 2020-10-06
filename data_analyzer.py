class Data_analyzer:
    def __init__(self, records):
        self.records = records

    def ec_pdb_split(self):
        ec_link = {}
        pdb_row = {}
        amount_row = 0
        for record in self.records:
            ec_sub_link = record.ec.split(';')
            ec = []
            for link in ec_sub_link:
                ec.append(link)
            ec_sub_link = record.ec.split(';')
            ec = []
            for link in ec_sub_link:
                ec.append(link)
            ec_link[record.number] = ec

            amount_row += 1
            sub_row = []
            pdbSubLink = record.pdb.split(';')
            amount = len(pdbSubLink)
            for i in range(amount):
                amount_row += 1
                pdb_information = []
                pdb_information.append(pdbSubLink[i])
                pdb_information.append(pdbSubLink[i].split('[')[0])
                sub_row.append(pdb_information)
            pdb_row[record.number] = sub_row

        return ec_link, pdb_row

    def substrate_product_split(self):
        sub = {}
        prod = {}
        for record in self.records:
            ex_link = record.pubchem_s  # 'https://pubchem.ncbi.nlm.nih.gov/compound/phloretin;https://pubchem.ncbi.nlm.nih.gov/compound/4-Nitrophenyl%20sulfate'
            sub_links = ex_link.split(';')
            flag = len(sub_links)
            ex = record.substrate  # 'phloretin;4-Nitrophenyl sulfate (quercetin/resveratrol/6-Hydroxyflavone); yes'
            subs = ex.split(';')
            length = len(subs)
            i = 0
            substrates = []
            while i < length:
                tuple = ["", "", ""]
                s_subs = subs[i].split('(')
                if len(s_subs) > 1:
                    tuple[0] = s_subs[0]
                    tuple[1] = "(" + s_subs[1]
                else:
                    tuple[0] = s_subs[0]
                if i < flag:
                    tuple[2] = sub_links[i]
                substrates.append(tuple)
                i += 1
            sub[record.number] = substrates

            ex_link = record.pubchem_p
            sub_links = ex_link.split(';')
            flag = len(sub_links)
            ex = record.product
            subs = ex.split(';')
            length = len(subs)
            i = 0
            product = []
            while i < length:
                tuple = ["", ""]
                tuple[0] = subs[i]
                if i < flag:
                    tuple[1] = sub_links[i]
                product.append(tuple)
                i += 1
            prod[record.number] = product

        return sub, prod
