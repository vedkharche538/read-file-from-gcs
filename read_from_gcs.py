from google.cloud import storage


def read_file_blob(bucket_name, destination_blob_name):
    """Read a file from the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # another way of downloading file from gcs bucket
    # read as string
    # read_output = blob.download_as_string()
    # download file to local
    blob.download_to_filename('filename')

    print(
        "File {} read successfully  from Bucket  {}.".format(
            destination_blob_name, bucket_name
        )
    )


read_file_blob('bucket_name',
               'destination_blob_name')

