==============================
API tutorials
==============================

New to using Lizard?
You have come to the right place: read this material to quickly get up and running.
Throughout this interactive manual for data scientists, we’ll walk you through basic Lizard API interactions.
Currently the following information is available:

For working in local environment, the required Python packages can be found in: `requirements.txt <https://github.com/nens/lizard-docs/blob/master/source/files/tutorials/requirements.txt>`_.

0. Jupyter Notebook kernel installation instructions
-----------------------------------------------------

For local development using Jupyter Notebook, it's recommended to create the Jupyter kernel in a Python virtual environment.
Once created and activated, packages can be installed in the environment with Conda or pip.
It is expected that Python and Jupyter Notebook are already installed.
Follow instructions explain the steps to install the kernel in the virtual environment.

1. Open a new terminal of the ``cmd`` command prompt.

2. Navigate to a directory where you want to install your virtual environment.

   - Navigate to a directory by running the command ``cd {directory}``.

3. Create the virtual environment in the selected directory.

   - Run: ``py -m venv {virtual environment name}``.

   - Example, run: ``py -m venv lizard``.

4. Activate the environment.

   - Run: ``./{virtual environment name}\Scripts\activate.bat"``.

   - You should now see ``({virtual environment name})`` before the terminal line.

5. Create a Jupyter kernel.

   - Run: ``ipython kernel install --user --name=lizard``.

6. Download the `requirements.txt <https://github.com/nens/lizard-docs/blob/master/source/files/tutorials/requirements.txt>`_.

   - Example: ``wget -O requirements.txt https://raw.githubusercontent.com/nens/lizard-docs/master/source/files/tutorials/requirements.txt``.

7. To install the packages.

   - Run: ``pip install -r \path\to\requirements.txt``.

   - Example: ``pip install -r C:\Users\steven\Downloads\requirements.txt``.

8. Open the Jupyter Notebook from inside the environment.
   - Run: ``jupyter notebook``.

Once Jupyter has started, open the preferred notebook.
The newly created kernel can be selected through the menu.

1. Interactive Time Series API manual
-----------------------------------------------------
For `/api/v4/timeseries` open `Google Colab Time Series <https://colab.research.google.com/github/nens/lizard-docs/blob/master/source/files/tutorials/Lizard_Time_Series_API_V4_Tutorial.ipynb>`_,
or download the `Jupyter Notebook Time Series <https://github.com/nens/lizard-docs/blob/master/source/files/tutorials/Lizard_Time_Series_API_V4_Tutorial.ipynb>`_.

2. Interactive Rasters API manual
-----------------------------------------------------
For `/api/v4/rasters` open `Google Colab Rasters <https://colab.research.google.com/github/nens/lizard-docs/blob/master/source/files/tutorials/Getting_familiair_with_Lizard_Rasters_API.ipynb>`_,
or download the `Jupyter Notebook Rasters <https://github.com/nens/lizard-docs/blob/master/source/files/tutorials/Getting_familiair_with_Lizard_Rasters_API.ipynb>`_.
Aditonally, download script `export_lizard_raster_layers.py <https://demo.lizard.net/media/tutorials/export_lizard_raster_layers.py>`_.

3. Interactive Retrieve Scenarios API manual
-----------------------------------------------------
For retrieving 3Di results / scenarios in Lizard, open `Google Colab Retrieve Scenarios <https://colab.research.google.com/github/nens/lizard-docs/blob/master/source/files/tutorials/How_to_download_a_maximum_waterdepth_raster_from_a_3Di_scenario_stored_in_the_Scenario_Archive_in_Lizard_.ipynb>`_,
or download the `Jupyter Notebook Retrieve Scenarios <https://github.com/nens/lizard-docs/blob/master/source/files/tutorials/How_to_download_a_maximum_waterdepth_raster_from_a_3Di_scenario_stored_in_the_Scenario_Archive_in_Lizard_.ipynb>`_.

.. note::
	API v4 is the stable API version. API v3 is deprecated since june 2023.
