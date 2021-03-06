from smartcard.util import toHexString

TAG_EF_COM  = 0x60
TAG_EF_DG1  = 0x61
TAG_EF_DG2  = 0x75
TAG_EF_DG3  = 0x63
TAG_EF_DG4  = 0x76
TAG_EF_DG5  = 0x65
TAG_EF_DG6  = 0x66
TAG_EF_DG7  = 0x67
TAG_EF_DG8  = 0x68
TAG_EF_DG9  = 0x69
TAG_EF_DG10 = 0x6a
TAG_EF_DG11 = 0x6b
TAG_EF_DG12 = 0x6c
TAG_EF_DG13 = 0x6d
TAG_EF_DG14 = 0x6e
TAG_EF_DG15 = 0x6f
TAG_EF_DG16 = 0x70
TAG_EF_SOD  = 0x77

FID_EF_COM  = 0x1e
FID_EF_DG1  = 0x01
FID_EF_DG2  = 0x02
FID_EF_DG3  = 0x03
FID_EF_DG4  = 0x04
FID_EF_DG5  = 0x05
FID_EF_DG6  = 0x06
FID_EF_DG7  = 0x07
FID_EF_DG8  = 0x08
FID_EF_DG9  = 0x09
FID_EF_DG10 = 0x0a
FID_EF_DG11 = 0x0b
FID_EF_DG12 = 0x0c
FID_EF_DG13 = 0x0d
FID_EF_DG14 = 0x0e
FID_EF_DG15 = 0x0f
FID_EF_DG16 = 0x10
FID_EF_SOD  = 0x1d
FID_EF_CARD_ACCESS = 0x1c

tags = {'t_bio_temp_count':     [0x02],
        't_tag_list':           [0x5C],
        't_lds_version' :       [0x5f,0x01],
        't_dob' :               [0x4f,0x08],
        't_disp_finger' :       [0x5f,0x09],
        't_enc_data_sec_feat' : [0x5f,0x0a],
        't_struc_sec_feat' :    [0x5f,0x0b],
        't_sec_feat' :          [0x5f,0x0c],
        't_full_name' :         [0x5f,0x0e],
        't_other_name' :        [0x5f,0x0f],
        't_personal_number' :   [0x5f,0x10],
        't_place_of_birth' :    [0x5f,0x11],
        't_telephone' :         [0x5f,0x12],
        't_profession' :        [0x5f,0x13],
        't_title' :             [0x5f,0x14],
        't_personal_summary' :  [0x5f,0x15],
        't_proof_citizenship' : [0x5f,0x16],
        't_other_valid_td_no' : [0x5f,0x17],
        't_custody_info' :      [0x5f,0x18],
        't_iss_auth'    :       [0x5f,0x19],
        't_other_ppl_doc' :     [0x5f,0x1a],
        't_endorsement' :       [0x5f,0x1b],
        't_tax_exit'    :       [0x5f,0x1c],
        't_doc_image_front' :   [0x5f,0x1d],
        't_doc_image_rear' :    [0x5f,0x1e],
        't_mrz_data_el'  :      [0x5f,0x1f],
        't_date_of_issue'  :    [0x5f,0x26],
        't_date_of_birth'  :    [0x5f,0x2b],
        't_bio_data_block'  :   [0x5f,0x2e],
        't_unicode_version'  :  [0x5f,0x36],
        't_comp_image_template':[0x5f,0x40],
        't_address'         :   [0x5f,0x42],
        't_image_signature' :   [0x5f,0x43],
        't_date_data_record' :  [0x5f,0x50],
        't_notify_person_name' :[0x5f,0x51],
        't_notify_person_phone':[0x5f,0x52],
        't_notify_person_add':  [0x5f,0x53],
        't_doc_info_date_time': [0x5f,0x55],
        't_doc_info_ser_no':    [0x5f,0x56],
        't_ef.com'      :       [0x60],
        't_mrz'      :          [0x61],
        't_finger_bio' :        [0x63],
        't_facial_image' :      [0x65],
        't_facial_digi_sig' :   [0x67],
        't_machine_assistance_enc_data' : [0x68],
        't_machine_assistance_structure' : [0x69],
        't_machine_assistance_substance' : [0x6a],
        't_add_personal_details' : [0x6b],
        't_add_doc_details' :   [0x6c],
        't_opt_details' :       [0x6d],
        't_rfu' :               [0x6e],
        't_person_to_notify' :  [0x70],
        't_facial_bio' :        [0x75],
        't_temp_iris' :         [0x76],
        't_ef.sod' :            [0x77],
        't_bio_data_block_ciphered' : [0x7f,0x2e],
        't_bio_info_template' : [0x7f,0x60],
        't_bio_info_group_template' : [0x7f,0x61]
        }

def gets(ls):
    ret = []
    for el in ls:
        val = tags.get(el)
        if(val != None):
            ret.add(val)
    return ret

def lookup(b):
    for key, val in tags.iteritems():
        if b == val:
            return key[2:]
    return ("unkown tag")