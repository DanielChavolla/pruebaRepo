import pandas as pd
import matplotlib.pyplot as plt
workbook1 = "GoldenData.csv"
valores = pd.read_excel(workbook1)
plt.xscale("log")

plt.plot(valores['Frequency'],valores['Lower'],color = 'Red')
plt.plot(valores['Frequency'],valores['Higher'], color = 'Red')
plt.plot(valores['Frequency'], valores['Muestra1'])
plt.plot(valores['Frequency'], valores['Muestra2'])
plt.plot(valores['Frequency'], valores['Muestra3'])
plt.plot(valores['Frequency'], valores['Muestra4'])
plt.plot(valores['Frequency'], valores['Muestra5'])
plt.plot(valores['Frequency'], valores['Muestra6'])
plt.plot(valores['Frequency'], valores['Muestra7'])
plt.plot(valores['Frequency'], valores['Muestra8'])
plt.plot(valores['Frequency'], valores['Muestra9'])
plt.plot(valores['Frequency'], valores['Muestra10'])
plt.plot(valores['Frequency'], valores['Muestra11'])
plt.plot(valores['Frequency'], valores['Muestra12'])
plt.plot(valores['Frequency'], valores['Muestra13'])
plt.plot(valores['Frequency'], valores['Muestra14'])
plt.plot(valores['Frequency'], valores['Muestra15'])
plt.plot(valores['Frequency'], valores['Muestra16'])
plt.plot(valores['Frequency'], valores['Muestra17'])
plt.plot(valores['Frequency'], valores['Muestra18'])
plt.plot(valores['Frequency'], valores['Muestra19'])
plt.plot(valores['Frequency'], valores['Muestra20'])
plt.plot(valores['Frequency'], valores['Muestra21'])
plt.plot(valores['Frequency'], valores['Muestra22'])
plt.plot(valores['Frequency'], valores['Muestra23'])
plt.plot(valores['Frequency'], valores['Muestra24'])
plt.plot(valores['Frequency'], valores['Muestra25'])
plt.plot(valores['Frequency'], valores['Muestra26'])
plt.plot(valores['Frequency'], valores['Muestra27'])
plt.plot(valores['Frequency'], valores['Muestra28'])
plt.plot(valores['Frequency'], valores['Muestra29'])
plt.plot(valores['Frequency'], valores['Muestra30'])
plt.plot(valores['Frequency'], valores['Muestra31'])
plt.plot(valores['Frequency'], valores['Muestra32'])
plt.plot(valores['Frequency'], valores['Muestra33'])
plt.xlabel('FREQUENCY')
plt.ylabel('F(w)')
plt.title('GOLDEN GOOD UNIT DATA')
plt.show()

def compareStatus():
    Compare1a = valores['Higher'] <= valores['Muestra1']
    for indice1a in Compare1a:
        if indice1a == True:
            indice_1a = [i1a for i1a, valor1a in enumerate(Compare1a) if valor1a]
            print('the values out of spec Higher on sample 1 are:', indice_1a)
        else:
            #print('UNDER SPEC 1A')
            break
    Compare1b = valores['Lower'] >= valores['Muestra1']
    for indice1b in Compare1b:
        if indice1b == True:
            indice_1b = [i1b for i1b, valor1b in enumerate(Compare1b) if valor1b]
            print('the values out of spec Lower on sample 1 are:', indice_1b)
        else:
            #print('UNDER SPEC 1B')
            break
    Compare2a = valores['Higher'] <= valores['Muestra2']
    for indice2a in Compare2a:
        if indice2a == True:
            indice_2a = [i2a for i2a, valor2 in enumerate(Compare2a) if valor2]
            print('the values out of spec Higher on sample 2 are:', indice_2a)
        else:
            #print('UNDER SPEC 2A')
            break
    Compare2b = valores['Lower'] >= valores['Muestra2']
    for indice2b in Compare2b:
        if indice2b == True:
            indice_2b = [i2b for i2b, valor2b in enumerate(Compare2b) if valor2b]
            print('the values out of spec Lower on sample 1 are:', indice_2b)
        else:
           # print('UNDER SPEC 2B')
            break
    Compare3a = valores['Higher'] <= valores['Muestra3']
    for indice3a in Compare3a:
        if indice3a == True:
            indice_3a = [i3a for i3a, valor3a in enumerate(Compare3a) if valor3a]
            print('the values out of spec Higher on sample 3 are:', indice_3a)
        else:
            #print('UNDER SPEC 3A')
            break
    Compare3b = valores['Lower'] >= valores['Muestra3']
    for indice3b in Compare3b:
        if indice3b == True:
            indice_3b = [i3b for i3b, valor3b in enumerate(Compare3b) if valor3b]
            print('the values out of spec Lower on sample 3 are:', indice_3b)
        else:
            #print('UNDER SPEC 3B')
            break
    Compare4a = valores['Higher'] <= valores['Muestra4']
    for indice4a in Compare4a:
        if indice4a == True:
            indice_4a = [i4a for i4a, valor4a in enumerate(Compare4a) if valor4a]
            print('the values out of spec Higher on sample 4 are:', indice_4a)
        else:
            #print('UNDER SPEC 4A')
            break
    Compare4b = valores['Lower'] >= valores['Muestra4']
    for indice4b in Compare4b:
        if indice4b == True:
            indice_4b = [i4b for i4b, valor4b in enumerate(Compare4b) if valor4b]
            print('the values out of spec Lower on sample 3 are:', indice_4b)
        else:
            #print('UNDER SPEC 4B')
            break
    Compare5a = valores['Higher'] <= valores['Muestra5']
    for indice5a in Compare5a:
        if indice5a == True:
            indice_5a = [i5a for i5a, valor5a in enumerate(Compare5a) if valor5a]
            print('the values out of spec Higher on sample 5 are:', indice_5a)
        else:
            #print('UNDER SPEC 5A')
            break
    Compare5b = valores['Lower'] >= valores['Muestra5']
    for indice5b in Compare5b:
        if indice5b == True:
            indice_5b = [i5b for i5b, valor5b in enumerate(Compare5b) if valor5b]
            print('the values out of spec Lower on sample 5 are:', indice_5b)
        else:
            #print('UNDER SPEC 5B')
            break
    Compare6a = valores['Higher'] <= valores['Muestra6']
    for indice6a in Compare6a:
        if indice6a == True:
            indice_6a = [i6a for i6a, valor6a in enumerate(Compare6a) if valor6a]
            print('the values out of spec Higher on sample 6 are:', indice_6a)
        else:
            #print('UNDER SPEC 6A')
            break
    Compare6b = valores['Lower'] >= valores['Muestra6']
    for indice6b in Compare6b:
        if indice6b == True:
            indice_6b = [i6b for i6b, valor6b in enumerate(Compare6b) if valor6b]
            print('the values out of spec Lower on sample 6 are:', indice_6b)
        else:
            #print('UNDER SPEC 6B')
            break
    Compare7a = valores['Higher'] <= valores['Muestra7']
    for indice7a in Compare7a:
        if indice7a == True:
            indice_7a = [i7a for i7a, valor7a in enumerate(Compare7a) if valor7a]
            print('the values out of spec Higher on sample 7 are:', indice_7a)
        else:
            #print('UNDER SPEC 7A')
            break
    Compare7b = valores['Lower'] >= valores['Muestra7']
    for indice7b in Compare7b:
        if indice7b == True:
            indice_7b = [i7b for i7b, valor7b in enumerate(Compare7b) if valor7b]
            print('the values out of spec Lower on sample 7 are:', indice_7b)
        else:
            #print('UNDER SPEC 7B')
            break
    Compare8a = valores['Higher'] <= valores['Muestra8']
    for indice8a in Compare8a:
        if indice8a == True:
            indice_8a = [i8a for i8a, valor8a in enumerate(Compare8a) if valor8a]
            print('the values out of spec Lower on sample 8 are:', indice_8a)
        else:
            #print('UNDER SPEC 8A')
            break
    Compare8b = valores['Lower'] >= valores['Muestra8']
    for indice8b in Compare8b:
        if indice8b == True:
            indice_8b = [i8b for i8b, valor8b in enumerate(Compare8b) if valor8b]
            print('the values out of spec Lower on sample 8 are:', indice_8b)
        else:
            #print('UNDER SPEC 8B')
            break
    Compare9a = valores['Higher'] <= valores['Muestra9']
    for indice9a in Compare9a:
        if indice9a == True:
            indice_9a = [i9a for i9a, valor9a in enumerate(Compare9a) if valor9a]
            print('the values out of spec Lower on sample 9 are:', indice_9a)
        else:
            #print('UNDER SPEC 9A')
            break
    Compare9b = valores['Lower'] >= valores['Muestra9']
    for indice9b in Compare9b:
        if indice9b == True:
            indice_9b = [i9b for i9b, valor9b in enumerate(Compare9b) if valor9b]
            print('the values out of spec Lower on sample 9 are:', indice_9b)
        else:
            #print('UNDER SPEC 9B')
            break
    Compare10a = valores['Higher'] <= valores['Muestra10']
    for indice10a in Compare10a:
        if indice10a == True:
            indice_10a = [i10a for i10a, valor10a in enumerate(Compare10a) if valor10a]
            print('the values out of spec Lower on sample 10 are:', indice_10a)
        else:
            #print('UNDER SPEC 10A')
            break
    Compare10b = valores['Lower'] >= valores['Muestra10']
    for indice10b in Compare10b:
        if indice10b == True:
            indice_10b = [i10b for i10b, valor10b in enumerate(Compare10b) if valor10b]
            print('the values out of spec Lower on sample 10 are:', indice_10b)
        else:
            #print('UNDER SPEC 10B')
            break
    Compare11a = valores['Higher'] <= valores['Muestra11']
    for indice11a in Compare11a:
        if indice11a == True:
            indice_11a = [i11a for i11a, valor11a in enumerate(Compare11a) if valor11a]
            print('the values out of spec Lower on sample 11 are:', indice_11a)
        else:
            #print('UNDER SPEC 11A')
            break
    Compare11b = valores['Lower'] >= valores['Muestra11']
    for indice11b in Compare11b:
        if indice11b == True:
            indice_11b = [i11b for i11b, valor11b in enumerate(Compare11b) if valor11b]
            print('the values out of spec Lower on sample 11 are:', indice_11b)
        else:
            #print('UNDER SPEC 11B')
            break
    Compare12a = valores['Higher'] <= valores['Muestra12']
    for indice12a in Compare12a:
        if indice12a == True:
            indice_12a = [i12a for i12a, valor12a in enumerate(Compare12a) if valor12a]
            print('the values out of spec Lower on sample 12 are:', indice_12a)
        else:
            #print('UNDER SPEC 12A')
            break
    Compare12b = valores['Lower'] >= valores['Muestra12']
    for indice12b in Compare12b:
        if indice12b == True:
            indice_12b = [i12b for i12b, valor12b in enumerate(Compare12b) if valor12b]
            print('the values out of spec Lower on sample 12 are:', indice_12b)
        else:
            #print('UNDER SPEC 12B')
            break
    Compare13a = valores['Higher'] <= valores['Muestra13']
    for indice13a in Compare13a:
        if indice13a == True:
            indice_13a = [i13a for i13a, valor13a in enumerate(Compare13a) if valor13a]
            print('the values out of spec Lower on sample 13 are:', indice_13a)
        else:
            #print('UNDER SPEC 13A')
            break
    Compare13b = valores['Lower'] >= valores['Muestra13']
    for indice13b in Compare13b:
        if indice13b == True:
            indice_13b = [i13b for i13b, valor13b in enumerate(Compare13b) if valor13b]
            print('the values out of spec Lower on sample 13 are:', indice_13b)
        else:
            #print('UNDER SPEC 13B')
            break
    Compare14a = valores['Higher'] <= valores['Muestra14']
    for indice14a in Compare14a:
        if indice14a == True:
            indice_14a = [i14a for i14a, valor14a in enumerate(Compare14a) if valor14a]
            print('the values out of spec Lower on sample 14 are:', indice_14a)
        else:
            #print('UNDER SPEC 14A')
            break
    Compare14b = valores['Lower'] >= valores['Muestra14']
    for indice14b in Compare14b:
        if indice14b == True:
            indice_14b = [i14 for i14b, valor14b in enumerate(Compare14b) if valor14b]
            print('the values out of spec Lower on sample 14 are:', indice_14b)
        else:
            #print('UNDER SPEC 14B')
            break
    Compare15a = valores['Higher'] <= valores['Muestra15']
    for indice15a in Compare15a:
        if indice15a == True:
            indice_15a = [i15a for i15a, valor15a in enumerate(Compare15a) if valor15a]
            print('the values out of spec Lower on sample 15 are:', indice_15a)
        else:
            #print('UNDER SPEC 15A')
            break
    Compare15b = valores['Lower'] >= valores['Muestra15']
    for indice15b in Compare15b:
        if indice15b == True:
            indice_15b = [i15b for i15b, valor15b in enumerate(Compare15b) if valor15b]
            print('the values out of spec Lower on sample 15 are:', indice_15b)
        else:
            #print('UNDER SPEC 15B')
            break
    Compare16a = valores['Higher'] <= valores['Muestra16']
    for indice16a in Compare16a:
        if indice16a == True:
            indice_16a = [i16a for i16a, valor16a in enumerate(Compare16a) if valor16a]
            print('the values out of spec Lower on sample 16 are:', indice_16a)
        else:
            #print('UNDER SPEC 16A')
            break
    Compare16b = valores['Lower'] >= valores['Muestra16']
    for indice16b in Compare16b:
        if indice16b == True:
            indice_16b = [i16b for i16b, valor16b in enumerate(Compare16b) if valor16b]
            print('the values out of spec Lower on sample 16 are:', indice_16b)
        else:
            #print('UNDER SPEC 16B')
            break
    Compare17a = valores['Higher'] <= valores['Muestra17']
    for indice17a in Compare17a:
        if indice17a == True:
            indice_17a = [i17a for i17a, valor17a in enumerate(Compare17a) if valor17a]
            print('the values out of spec Lower on sample 17 are:', indice_17a)
        else:
            #print('UNDER SPEC 17A')
            break
    Compare17b = valores['Lower'] >= valores['Muestra17']
    for indice17b in Compare17b:
        if indice17b == True:
            indice_17b = [i17b for i17b, valor17b in enumerate(Compare17b) if valor17b]
            print('the values out of spec Lower on sample 17 are:', indice_17b)
        else:
            #print('UNDER SPEC 17B')
            break
    Compare18a = valores['Higher'] <= valores['Muestra18']
    for indice18a in Compare18a:
        if indice18a == True:
            indice_18a = [i18a for i18a, valor18a in enumerate(Compare18a) if valor18a]
            print('the values out of spec Lower on sample 18 are:', indice_18a)
        else:
            #print('UNDER SPEC 18A')
            break
    Compare18b = valores['Lower'] >= valores['Muestra18']
    for indice18b in Compare18b:
        if indice18b == True:
            indice_18b = [i18b for i18b, valor18b in enumerate(Compare18b) if valor18b]
            print('the values out of spec Lower on sample 18 are:', indice_18b)
        else:
            #print('UNDER SPEC 18B')
            break
    Compare19a = valores['Higher'] <= valores['Muestra19']
    for indice19a in Compare19a:
        if indice19a == True:
            indice_19a = [i19a for i19a, valor19a in enumerate(Compare19a) if valor19a]
            print('the values out of spec Lower on sample 19 are:', indice_19a)
        else:
            #print('UNDER SPEC 19A')
            break
    Compare19b = valores['Lower'] >= valores['Muestra19']
    for indice19b in Compare19b:
        if indice19b == True:
            indice_19b = [i19b for i19b, valor19b in enumerate(Compare19b) if valor19b]
            print('the values out of spec Lower on sample 19 are:', indice_19b)
        else:
            #print('UNDER SPEC 19B')
            break
    Compare20a = valores['Higher'] <= valores['Muestra20']
    for indice20a in Compare20a:
        if indice20a == True:
            indice_20a = [i20a for i20a, valor20a in enumerate(Compare20a) if valor20a]
            print('the values out of spec Lower on sample 20 are:', indice_20a)
        else:
            #print('UNDER SPEC 20A')
            break
    Compare20b = valores['Lower'] >= valores['Muestra20']
    for indice20b in Compare20b:
        if indice20b == True:
            indice_20b = [i20b for i20b, valor20b in enumerate(Compare20b) if valor20b]
            print('the values out of spec Lower on sample 20 are:', indice_20b)
        else:
            #print('UNDER SPEC 20B')
            break
    Compare21a = valores['Higher'] <= valores['Muestra21']
    for indice21a in Compare21a:
        if indice21a == True:
            indice_21a = [i21a for i21a, valor21a in enumerate(Compare21a) if valor21a]
            print('the values out of spec Lower on sample 21 are:', indice_21a)
        else:
            #print('UNDER SPEC 21A')
            break
    Compare21b = valores['Lower'] >= valores['Muestra21']
    for indice21b in Compare21b:
        if indice21b == True:
            indice_21b = [i21b for i21b, valor21b in enumerate(Compare21b) if valor21b]
            print('the values out of spec Lower on sample 21 are:', indice_21b)
        else:
            #print('UNDER SPEC 21B')
            break
    Compare22a = valores['Higher'] <= valores['Muestra22']
    for indice22a in Compare22a:
        if indice22a == True:
            indice_22a = [i22a for i22a, valor22a in enumerate(Compare22a) if valor22a]
            print('the values out of spec Lower on sample 22 are:', indice_22a)
        else:
            #print('UNDER SPEC 22A')
            break
    Compare22b = valores['Lower'] >= valores['Muestra22']
    for indice22b in Compare22b:
        if indice22b == True:
            indice_22b = [i22b for i22b, valor22b in enumerate(Compare22b) if valor22b]
            print('the values out of spec Lower on sample 22 are:', indice_22b)
        else:
            #print('UNDER SPEC 22B')
            break
    Compare23a = valores['Higher'] <= valores['Muestra23']
    for indice23a in Compare23a:
        if indice23a == True:
            indice_23a = [i23a for i23a, valor23a in enumerate(Compare23a) if valor23a]
            print('the values out of spec Lower on sample 23 are:', indice_23a)
        else:
            #print('UNDER SPEC 23A')
            break
    Compare23b = valores['Lower'] >= valores['Muestra23']
    for indice23b in Compare23b:
        if indice23b == True:
            indice_23b = [i23b for i23b, valor23b in enumerate(Compare23b) if valor23b]
            print('the values out of spec Lower on sample 23 are:', indice_23b)
        else:
            #print('UNDER SPEC 23B')
            break
    Compare24a = valores['Higher'] <= valores['Muestra24']
    for indice24a in Compare24a:
        if indice24a == True:
            indice_24a = [i24a for i24a, valor24a in enumerate(Compare24a) if valor24a]
            print('the values out of spec Lower on sample 24 are:', indice_24a)
        else:
            #print('UNDER SPEC 24A')
            break
    Compare24b = valores['Lower'] >= valores['Muestra24']
    for indice24b in Compare24b:
        if indice24b == True:
            indice_24b = [i24b for i24b, valor24b in enumerate(Compare24b) if valor24b]
            print('the values out of spec Lower on sample 24 are:', indice_24b)
        else:
            #print('UNDER SPEC 24B')
            break
    Compare25a = valores['Higher'] <= valores['Muestra25']
    for indice25a in Compare25a:
        if indice25a == True:
            indice_25a = [i25a for i25a, valor25a in enumerate(Compare25a) if valor25a]
            print('the values out of spec Lower on sample 25 are:', indice_25a)
        else:
            #print('UNDER SPEC 25A')
            break
    Compare25b = valores['Lower'] >= valores['Muestra25']
    for indice25b in Compare25b:
        if indice25b == True:
            indice_25b = [i25b for i25b, valor25b in enumerate(Compare25b) if valor25b]
            print('the values out of spec Lower on sample 25 are:', indice_25b)
        else:
            #print('UNDER SPEC 25B')
            break
    Compare26a = valores['Higher'] <= valores['Muestra26']
    for indice26a in Compare26a:
        if indice26a == True:
            indice_26a = [i26a for i26a, valor26a in enumerate(Compare26a) if valor26a]
            print('the values out of spec Lower on sample 26 are:', indice_26a)
        else:
            #print('UNDER SPEC 26A')
            break
    Compare26b = valores['Lower'] >= valores['Muestra26']
    for indice26b in Compare26b:
        if indice26b == True:
            indice_26b = [i26b for i26b, valor26b in enumerate(Compare26b) if valor26b]
            print('the values out of spec Lower on sample 26 are:', indice_26b)
        else:
            #print('UNDER SPEC 26B')
            break
    Compare27a = valores['Higher'] <= valores['Muestra27']
    for indice27a in Compare27a:
        if indice27a == True:
            indice_27a = [i27a for i27a, valor27a in enumerate(Compare27a) if valor27a]
            print('the values out of spec Lower on sample 27 are:', indice_27a)
        else:
            #print('UNDER SPEC 27A')
            break
    Compare27b = valores['Lower'] >= valores['Muestra27']
    for indice27b in Compare27b:
        if indice17b == True:
            indice_27b = [i27b for i27b, valor27b in enumerate(Compare27b) if valor27b]
            print('the values out of spec Lower on sample 27 are:', indice_27b)
        else:
            #print('UNDER SPEC 27B')
            break
    Compare28a = valores['Higher'] <= valores['Muestra28']
    for indice28a in Compare28a:
        if indice28a == True:
            indice_28a = [i28a for i28a, valor28a in enumerate(Compare28a) if valor28a]
            print('the values out of spec Lower on sample 28 are:', indice_28a)
        else:
            #print('UNDER SPEC 28A')
            break
    Compare28b = valores['Lower'] >= valores['Muestra28']
    for indice28b in Compare28b:
        if indice28b == True:
            indice_28b = [i28b for i28b, valor28b in enumerate(Compare28b) if valor28b]
            print('the values out of spec Lower on sample 28 are:', indice_28b)
        else:
            #print('UNDER SPEC 28B')
            break
    Compare29a = valores['Higher'] <= valores['Muestra29']
    for indice29a in Compare29a:
        if indice29a == True:
            indice_29a = [i29a for i29a, valor29a in enumerate(Compare29a) if valor29a]
            print('the values out of spec Lower on sample 29 are:', indice_29a)
        else:
            #print('UNDER SPEC 29A')
            break
    Compare29b = valores['Lower'] >= valores['Muestra29']
    for indice29b in Compare29b:
        if indice29b == True:
            indice_29b = [i29b for i29b, valor29b in enumerate(Compare29b) if valor29b]
            print('the values out of spec Lower on sample 29 are:', indice_29b)
        else:
            #print('UNDER SPEC 29B')
            break
    Compare30a = valores['Higher'] <= valores['Muestra30']
    for indice30a in Compare30a:
        if indice30a == True:
            indice_30a = [i30a for i30a, valor30a in enumerate(Compare30a) if valor30a]
            print('the values out of spec Lower on sample 30 are:', indice_30a)
        else:
            #print('UNDER SPEC 30A')
            break
    Compare30b = valores['Lower'] >= valores['Muestra30']
    for indice30b in Compare30b:
        if indice30b == True:
            indice_30b = [i30b for i30b, valor30b in enumerate(Compare30b) if valor30b]
            print('the values out of spec Lower on sample 30 are:', indice_30b)
        else:
            #print('UNDER SPEC 30B')
            break
    Compare31a = valores['Higher'] <= valores['Muestra31']
    for indice31a in Compare31a:
        if indice31a == True:
            indice_31a = [i31a for i31a, valor31a in enumerate(Compare31a) if valor31a]
            print('the values out of spec Lower on sample 31 are:', indice_31a)
        else:
            #print('UNDER SPEC 31A')
            break
    Compare31b = valores['Lower'] >= valores['Muestra31']
    for indice31b in Compare31b:
        if indice31b == True:
            indice_31b = [i31b for i31b, valor31b in enumerate(Compare31b) if valor31b]
            print('the values out of spec Lower on sample 31 are:', indice_31b)
        else:
            #print('UNDER SPEC 31B')
            break
    Compare32a = valores['Higher'] <= valores['Muestra32']
    for indice32a in Compare32a:
        if indice32a == True:
            indice_32a = [i32a for i32a, valor32a in enumerate(Compare32a) if valor32a]
            print('the values out of spec Lower on sample 32 are:', indice_32a)
        else:
            #print('UNDER SPEC 32A')
            break
    Compare32b = valores['Lower'] >= valores['Muestra32']
    for indice32b in Compare32b:
        if indice32b == True:
            indice_32b = [i32b for i32b, valor32b in enumerate(Compare32b) if valor32b]
            print('the values out of spec Lower on sample 32 are:', indice_32b)
        else:
            #print('UNDER SPEC 32B')
            break
    Compare33a = valores['Higher'] <= valores['Muestra33']
    for indice33a in Compare33a:
        if indice33a == True:
            indice_33a = [i33a for i33a, valor33a in enumerate(Compare33a) if valor33a]
            print('the values out of spec Lower on sample 33 are:', indice_33a)
        else:
            #print('UNDER SPEC 33A')
            break
    Compare33b = valores['Lower'] >= valores['Muestra33']
    for indice33b in Compare33b:
        if indice33b == True:
            indice_33b = [i33b for i33b, valor33b in enumerate(Compare33b) if valor33b]
            print('the values out of spec Lower on sample 33 are:', indice_33b)
        else:
            #print('UNDER SPEC 33B')
            break

compareStatus()
