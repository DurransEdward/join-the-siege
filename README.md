# Heron Coding Challenge - File Classifier

## My Approach

With the time constraint, I decided to implement a quick, but also accurate and robust, solution: send the documents to openAI's `gpt-4o-mini` API to be classified. This model is highly versatile and can be used for a wide range of tasks, including document classification. Setting the `response_format` field in the request guarantees the response will be the required format.

## Running the Code

1. Clone the repository:
    ```shell
    git clone <repository_url>
    cd join-the-siege
    ```

2. Create virtual environment and install dependencies:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    brew install poppler
    ```

3. Create a `.env` file in the root directory of the project with the following content:
    ```shell
    OPENAI_API_KEY='your-openai-api-key'
    ```
    Go to https://platform.openai.com to make an OpenAI account and create an API key.

4. Run the Flask app:
    ```shell
    python -m src.app
    ```

5. Test the classifier using curl:
    ```shell
    curl -X POST -F 'file=@path_to_pdf.pdf' http://127.0.0.1:5000/classify_file
    ```

6. Run tests:
   ```shell
    pytest
    ```

## Test Results

The classifier correctly classifies all the documents in the `tests/test_data/files` directory. This directory includes a variety of content types: PDFs, JPEGs, PNGs, and a variety of document classes: bank statements, invoices, drivers licences, resumes, and a photograph of a cat (which the classifier correctly identifies as an `unknown file` since it isn't a document). This directory also includes a file with a deliberately named with a misleading name (invoice_5.pdf when the document is actually a bank statement), the classifier correctly classifies this document nonetheless.

## Scalability

Since the `gpt-4o-mini` is extremely versatile, the current classifier is highly scalable to new industries and new document classes. For example, if you wanted the classifier to be able to classify receipts, you can simply add `receipts` to the `DOCUMENT_CLASSES` list in `src/config.py`.

Moreover, using OpenAI's `gpt-4o-mini` model, the current classifier is highly scalable in terms of cost. Each request uses ~1000 tokens (https://platform.openai.com/docs/guides/vision#calculating-costs) and it costs just $0.15 per 1,000,000 tokens (https://openai.com/api/pricing). This means that it costs approximately just $0.15 per 1000 requests.

## Limitations and Weaknesses (Areas for Improvement)

Currently, the classifier is only able to handle JPEG, PNG, and PDF files. This is because the OpenAI API only accepts PNGs, JPEGs and static GIFs (and the conversion from PDF to JPEG is very simple). With more time, I would have added support for more file types by converting them to PNGs or JPEGs before sending them to the API.

Since the classifier relies on a third party API, it is vulnerable to failure if that API goes down or malfunctions. This could be mitigated by implementing a fallback classifier. Alternatively, if requests do not need to be handled quickly, they could be sent to a queue which will be processed when the API is up and working properly.

## Running in Production

Suggestions for running the code in production:

- Run the app on a cloud server with built-in horizontal scaling, such as AWS Elastic Beanstalk. This will allow the app to automatically scale up or down based on the number of requests.
- Consider changing the request router framework from Flask to a request router framework which can handle multiple requests asynchronously, such as Quart. This will allow the app to handle more requests at the same time, improving performance.
- Set up GitHub Actions to automatically run tests on every push to the repository.

## Final Comments

With more time, I would have liked to have built my own classifier by fine tuning an existing open-source image recognition model, probably from the transformers library. My choice to use the OpenAI API was to meet the time constraint.