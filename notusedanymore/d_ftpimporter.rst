==============================
FTP Importer
==============================

Using the Lizard FTP
++++++++++++++++++++ 

The examples below elaborate on how to supply raster data to the Lizard FTP and how to manage your data flow to Lizard.
Because data uploads depend on the system configuration of the data provider, we provide a code example to make a tool for automatic uploads.

* You can do this using the python FTPlib package (example 1).
* You can also use 'curl' from your commandline (example 2).

When using the FTP your raster filename should contain either the RasterSource uuid or the configured 'Supplier code' in the filename.
The user that uploads the data should also be configured as the Supplier for the RasterSource.

Example 1 using python FTPlib package
_____________________________________

.. code-block:: python

    import ftplib
    import getpass
    import os

    LIZARD_USERNAME = input('Lizard username: ')
    LIZARD_PASSWORD = getpass.getpass('Lizard password: ')


    filename = "d1e25b6b-d777-4c90-a067-45645ed40da7_2018-02-13T122056Z.geotiff"
    file_path = "D:/data/" + filename
    file_path

    os.path.exists(file_path)

    file = open(file_path, 'rb')
    ftp = ftplib.FTP_TLS()
    host = "ftpdata.lizard.net"
    port = 21
    ftp.connect(host, port)
    print(ftp.getwelcome())
    ftp.login(LIZARD_USERNAME, LIZARD_PASSWORD)
    ftp.prot_p()
    ftp.storbinary("STOR " + filename, file)
    ftp.close()


Example 2 using 'curl' from your commandline 
____________________________________________

.. code-block:: python

    import os

    def raster_to_ftp(file_path, filename):
        log.info(file_path)
        ftp_login = "ftp://{}:{}@ftpdata.lizard.net/".format(LIZARD_USERNAME, LIZARD_PASSWORD)
        curl_command = "curl --ssl -T {} {}".format(file_path, ftp_login)
        os.system(curl_command)
        os.remove(file_path)
        log.info('files sent to ftp')

    filenames = ["d1e25b6b-d777-4c90-a067-45645ed40da7_2018-02-12T122056Z.geotiff", 
                "d1e25b6b-d777-4c90-a067-45645ed40da7_2018-02-13T122056Z.geotiff"]

    for filename in filenames:
        file_path = "D:/data/" + filename
        raster_to_ftp(file_path, filename)