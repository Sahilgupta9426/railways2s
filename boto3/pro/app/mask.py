#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from numpy import append

def detect_labels(photo):
    Image=photo
    # photo=open(photo,'rb')
    client = boto3.client('rekognition',aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')

    response = client.detect_protective_equipment(Image={'Bytes': Image.read()}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
        
    detect_labels.resp=response
    # print('Detected PPE for people in image ',  Image) 
    print('\nDetected people\n---------------')
    list1=[]   
    for person in response['Persons']:
        
        print('Person ID: ' + str(person['Id']))
        print ('Body Parts\n----------')
        body_parts = person['BodyParts']
        if len(body_parts) == 0:
                print ('No body parts found')
                fs=f'No body parts found'
                list1.append(fs)
        else:
            for body_part in body_parts:
                print('\t'+ body_part['Name'] + '\n\t\tConfidence: ' + str(body_part['Confidence']))
                bp=body_part['Name']
                bpc=str(body_part['Confidence'])
                fs1=f'\t {bp}  \n\t\tConfidence: {bpc}'
                list1.append(fs1)
                print('\n\t\tDetected PPE\n\t\t------------')
                info=f'\n\t\tDetected PPE\n\t\t------------'
                
                ppe_items = body_part['EquipmentDetections']
                if len(ppe_items) ==0:
                    bname=body_part['Name']
                    nppe=f'\t\tNo PPE detected on {bname}'
                    list1.append(nppe)
                    print ('\t\tNo PPE detected on ' + body_part['Name'])
                else:    
                    for ppe_item in ppe_items:
                        print('\t\t' + ppe_item['Type'] + '\n\t\t\tConfidence: ' + str(ppe_item['Confidence']))
                        ppei= ppe_item['Type']
                        ppi2=str(ppe_item['Confidence'])
                        ppe3=f'\t\t {ppei} \n\t\t\tConfidence: {ppi2}'
                        list1.append(ppe3)
                        print('\t\tCovers body part: ' + str(ppe_item['CoversBodyPart']['Value']) + '\n\t\t\tConfidence: ' 
                        + str(ppe_item['CoversBodyPart']['Confidence']))
                        pi1= str(ppe_item['CoversBodyPart']['Value'])
                        pi2=str(ppe_item['CoversBodyPart']['Confidence'] )
                        fppe=f'\t\tCovers body part: {pi1} \n\t\t\tConfidence: {pi2}'
                        list1.append(fppe)
                        print('\t\tBounding Box:')
                        bb=f'\t\tBounding Box:'
                        list1.append(bb)
                        print ('\t\t\tTop: ' + str(ppe_item['BoundingBox']['Top']))
                        top=str(ppe_item['BoundingBox']['Top'])
                        t1=f'\t\t\tTop: {top}'
                        list1.append(t1)
                        print ('\t\t\tLeft: ' + str(ppe_item['BoundingBox']['Left']))
                        left=str(ppe_item['BoundingBox']['Left'])
                        l=f'\t\t\tLeft:{left}'
                        list1.append(l)
                        print ('\t\t\tWidth: ' +  str(ppe_item['BoundingBox']['Width']))
                        width=str(ppe_item['BoundingBox']['Width'])
                        wf=f'\t\t\tWidth: {width}'
                        list1.append(wf)
                        print ('\t\t\tHeight: ' +  str(ppe_item['BoundingBox']['Height']))

                        height=str(ppe_item['BoundingBox']['Height'])
                        h1=f'\t\t\tHeight: {height}'
                        list1.append(h1)
                        print ('\t\t\tConfidence: ' + str(ppe_item['Confidence']))
                        con=str(ppe_item['Confidence'])
                        cf=f'\t\t\tConfidence: {con}'
                        list1.append(cf)
            print()
        print()
    detect_labels.informations=list1
    print('Person ID Summary\n----------------')
    display_summary('With required equipment',response['Summary']['PersonsWithRequiredEquipment'] )
    display_summary('Without required equipment',response['Summary']['PersonsWithoutRequiredEquipment'] )
    display_summary('Indeterminate',response['Summary']['PersonsIndeterminate'] )
   
    print()
    # photo.close()
    return len(response['Persons'])

#Display summary information for supplied summary.
def display_summary(summary_type, summary):
    print (summary_type + '\n\tIDs: ',end='')
    if (len(summary)==0):
        print('None')
    else:
        for num, id in enumerate(summary, start=0):
            if num==len(summary)-1:
                print (id)
            else:
                print (str(id) + ', ' , end='')



def main():
    photo='photo1.jpg'
    bucket=''
    person_count=detect_labels(photo)
    print("Persons detected: " + str(person_count))


if __name__ == "__main__":
    main()


