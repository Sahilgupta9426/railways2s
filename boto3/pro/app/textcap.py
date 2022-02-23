import boto3

def detect_text(photo, bucket):

    client = boto3.client('rekognition',aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')

    Image=photo

    response=client.detect_text(Image={'Bytes': Image.read()})
                        
    textDetections=response['TextDetections']
    detect_text.textdetected=response['TextDetections']
    print ('Detected text\n----------')
    list1=[]
    for text in textDetections:
            print(text['DetectedText'])
            list1.append(text['DetectedText'])
            #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            #print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                #print ('Parent Id: {}'.format(text['ParentId']))
                pass
            #print ('Type:' + text['Type'])
            print()
    # print("myresult:",text)
    detect_text.list1=list1
    return len(textDetections)

def main():

    bucket=''
    photo='reviews.png'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()