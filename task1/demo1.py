one_data_dict = {"originalText": "入院前4年患者院外测血压高，最高达230/？mmHg，院外服用坎地沙坦、氨氯地平、卡维地洛药物控制血压（具体剂量不详），院外自测血压约150-160mmHg，平素未感视物模糊，未感头昏。2天前患者骑车时不慎跌倒，至两膝、两手掌、上巴处擦伤，感头昏痛，遂于我院门诊就诊，查血压170/100mmHg，血脂：甘油三酯 3.72 mmol/l ↑、总胆固醇 6.26 mmol/l ↑、载脂蛋白B 1.48 g/l ↑，血糖(静脉血)：葡萄糖 9.27 mmol/l ↑，肝功1：谷丙转氨酶 34.3 U/L、谷草转氨酶 20.9 U/L、谷氨酰转肽酶 112.6 U/L ↑，血常规：白细胞数 4.6×10^9/L、红细胞数 5.24×10^12/L、血红蛋白浓度 160 g/L、血小板数 256×10^9/L、中性粒细胞百分比 57.80 %、淋巴细胞百分比 35.90 %，肾功能未见异常，予以硝苯地平缓释片降压处理后好转。1天前患者感头昏减轻，再次于我院就诊，查糖化血红蛋白：糖化血红蛋白 8.7 %，血糖(静脉血)：葡萄糖 13.90 mmol/l，尿微量白蛋白定量：尿微量白蛋白 451 mg/L，尿常规：酮体 -、尿胆原 +、蛋白 +、葡萄糖 +++。无意识障碍大小便失禁，无肢体活动受限，否认多饮多食，否认多尿消瘦，无胸闷胸痛，无腹胀腹痛，无上肢水肿，为进一步治疗，门诊以“高血压、糖尿病”收入我科住院治疗。病程中患者精神、饮食一般，大小便正常，体重无明显上降。", "entities": [{"label_type": "药物", "overlap": 0, "start_pos": 31, "end_pos": 35}, {"label_type": "药物", "overlap": 0, "start_pos": 36, "end_pos": 40}, {"label_type": "药物", "overlap": 0, "start_pos": 41, "end_pos": 45}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 90, "end_pos": 91}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 107, "end_pos": 109}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 110, "end_pos": 113}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 114, "end_pos": 116}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 121, "end_pos": 122}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 152, "end_pos": 156}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 171, "end_pos": 175}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 190, "end_pos": 195}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 215, "end_pos": 218}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 237, "end_pos": 242}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 252, "end_pos": 257}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 267, "end_pos": 273}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 290, "end_pos": 293}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 306, "end_pos": 309}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 324, "end_pos": 330}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 339, "end_pos": 342}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 355, "end_pos": 363}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 372, "end_pos": 379}, {"label_type": "药物", "overlap": 0, "start_pos": 398, "end_pos": 405}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 419, "end_pos": 420}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 440, "end_pos": 446}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 461, "end_pos": 464}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 487, "end_pos": 493}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 507, "end_pos": 509}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 512, "end_pos": 515}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 518, "end_pos": 520}, {"label_type": "实验室检验", "overlap": 0, "start_pos": 523, "end_pos": 526}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 543, "end_pos": 545}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 565, "end_pos": 566}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 567, "end_pos": 568}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 571, "end_pos": 572}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 573, "end_pos": 574}, {"label_type": "解剖部位", "overlap": 0, "start_pos": 577, "end_pos": 579}, {"label_type": "疾病和诊断", "overlap": 0, "start_pos": 593, "end_pos": 596}, {"label_type": "疾病和诊断", "overlap": 0, "start_pos": 597, "end_pos": 600}]}
class data_preprocess(object):
    """
    输入一行字典形式的原始数据，返回originalText_list, label_list
    """
    def __init__(self, one_data_dict):
        self.one_data_dict = one_data_dict
    def get_label_cn2eng(self, entity):
        label_B = ''
        label_I = ''
        if entity['label_type'] == '疾病和诊断':
            label_B = 'disease_diagnosis_B'
            label_I = 'disease_diagnosis_I'
        elif entity['label_type'] == '检查':
            label_B = 'inspect_B'
            label_I = 'inspect_I'
        elif entity['label_type'] == '检验':
            label_B = 'examination_B'
            label_I = 'examination_I'
        elif entity['label_type'] == '手术':
            label_B = 'surgery_B'
            label_I = 'surgery_I'
        elif entity['label_type'] == '药物':
            label_B = 'medicine_B'
            label_I = 'medicine_I'
        elif entity['label_type'] == '解剖部位':
            label_B = 'anatomy_B'
            label_I = 'anatomy_I'
        label_B_index = entity['start_pos']
        label_I_index = entity['end_pos']
        return label_B, label_I, label_B_index, label_I_index

    def get_BIO(self):
        originalText_list = list(self.one_data_dict['originalText'])
        # print(originalText_list)
        entities_list = self.one_data_dict['entities']
        label_list = ['O'] * len(originalText_list)
        for entity in entities_list:
            label_B, label_I, label_B_index, label_I_index = self.get_label_cn2eng(entity)
            if label_I_index - label_B_index == 1:
                label_list[label_B_index] = label_B
            else:
                label_list[label_B_index] = label_B
                label_list[label_I_index - 1] = label_I
                for i in range(label_B_index + 1, label_I_index - 1):
                    label_list[i] = label_I
        return originalText_list, label_list

data = data_preprocess(one_data_dict)
originalText_list, label_list = data.get_BIO()
for i in range(len(label_list)):
    print(originalText_list[i] + ' ' + label_list[i])
