from flask import Flask, render_template, request
from werkzeug.datastructures import FileStorage

from factories.ContentTypeToImporterFactory import ContentTypeToImporterFactory, ContentTypeToImporterWithPrimitiveTypesFactory

app = Flask(__name__)

# content_type_to_importer_factory = ContentTypeToImporterFactory()
content_type_to_importer_factory = ContentTypeToImporterWithPrimitiveTypesFactory()

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f: FileStorage = request.files['file']
        importer = content_type_to_importer_factory.get_importer(f.content_type)
        print(importer.get_data_from_stream(f.stream))

        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
