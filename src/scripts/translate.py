import os
from google.cloud import translate_v2 as translate


if __name__ == '__main__':
    # set up the translation client
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key.json'
    translate_client = translate.Client()
    # specify the directory containing the text files
    input_directory = './data/elections/estonian/'
    # specify the output directory for the translated files
    output_directory = './data/elections/english/'

    for subdir, dirs, files in os.walk(input_directory):
        for filename in files:
            filepath = os.path.join(subdir, filename)
            # only process .txt files
            if filepath.endswith('.txt'):
                input_file_path = filepath
                output_file_path = os.path.join(output_directory, filename)
                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    text = input_file.read()
                    # translate the text from Estonian to English
                    try:
                        result = translate_client.translate(text, target_language='en', format_='text')
                    except Exception as e:
                        print(e)
                        continue
                    # write the translated text to the output file
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(result['translatedText'])
