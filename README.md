# 🎥 Video Frame Extractor

[🇪🇸 Español](README.es.md)

A Python-based tool for extracting frames from one or more videos at configurable time intervals.

This project was created as an **auxiliary tool for computer vision projects**, allowing video files to be converted into individual images that can later be reviewed, selected, labelled and used to create image datasets.

---

## 🧠 What problem does it solve?

When working on computer vision projects, data is often collected and stored in video format.

However, many computer vision tasks require individual images rather than complete video files.

For example:

```text
🎥 Video
   │
   ▼
Video Frame Extractor
   │
   ▼
🖼️ 🖼️ 🖼️ 🖼️ 🖼️
Individual frames
```

This tool automates the extraction of individual images from videos using a configurable time interval.

It can be useful for preparing image data for:

- Object detection.
- Image classification.
- Dataset creation.
- Computer vision research.
- Machine learning projects.

> **Note:** This tool only extracts and organises video frames. It does not perform object detection, image classification or automatic image labelling.

---

## ✨ Features

- Selection of one or more videos.
- Selection of the destination folder.
- Configurable extraction interval.
- Minimum extraction interval of **0.5 seconds**.
- Default extraction interval of **2 seconds**.
- Automatic creation of a `frames` folder.
- Extraction of frames in `.jpg` format.
- Consecutive frame numbering throughout the entire execution.
- Processing of multiple videos in a single execution.
- Retrieval of basic information about each video.
- Automatic generation of a processing report in `.txt` format.
- Display of processing results in the console.

### Supported video formats

The file selection interface currently supports the following formats:

```text
.mp4
.avi
.mov
.mkv
.webm
```

> Actual compatibility may depend on the video codec, encoding and version of OpenCV installed on the system.

---

## 📸 How does it work?

### 1. Select the videos

First, a file selection window is displayed, allowing one or more videos to be selected.

![Video selection](assets/images/select_video.jpg)

The programme allows multiple files to be selected and processed during a single execution.

---

### 2. Create a folder for the results

It is recommended to create a separate folder for each processing session. This helps keep the generated frames and reports organised and makes it easier to identify the results associated with each processing session.

For example, a folder called:

```text
Capturas/
```

can be created.

![Create a folder for the results](assets/images/new_file.jpg)

Once the folder has been created, a name can be assigned to it to make the processing session or the set of videos being processed easier to identify.

![Name the results folder](assets/images/name_file.jpg)

This folder will be used as the destination location. The programme will automatically create a folder called `frames` inside it, where the extracted frames will be stored.

The resulting structure will be similar to the following:

```text
Capturas/
│
├── frames/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   ├── frame_0003.jpg
│   └── ...
│
└── reporte_frames_YYYYMMDD_HHMMSS.txt
```

![Organisation of the generated files](assets/images/result_frames.jpg)

> **Recommendation:** using a separate folder for each processing session helps keep the extracted frames and generated reports organised, while also making it easier to identify the results associated with each session.

---

### 3. Select the destination folder

After selecting the videos, the programme asks for the folder where the extracted frames will be stored.

![Destination folder selection](assets/images/select_file.jpg)

A `frames` folder will be created automatically inside the selected location.

---

### 4. Configure the extraction interval

The programme then asks how often a frame should be extracted, in seconds.

![Extraction interval](assets/images/select_time_seconds.jpg)

The default value is:

```text
2.0 seconds
```

The minimum allowed value is:

```text
0.5 seconds
```

For example:

| Interval | Approximate extraction |
|---:|---|
| `2.0 s` | 1 frame every 2 seconds |
| `1.0 s` | 1 frame every second |
| `0.5 s` | 1 frame every half second |

The interval must be a numerical value equal to or greater than `0.5` seconds.

---

### 5. Frame extraction

Once the configuration has been completed, the programme begins processing the selected videos.

![Start of the processing](assets/images/start_script.jpg)

Each extracted frame is saved as a `.jpg` file inside the `frames` folder.

The files use consecutive numbering:

```text
frame_0001.jpg
frame_0002.jpg
frame_0003.jpg
...
```

The numbering starts at `0001` and continues throughout the entire execution.

---

### 6. Processing multiple videos

Multiple videos can be processed during a single execution.

When several files are processed, frame numbering continues from one video to the next.

For example, if the first video generates:

```text
frame_0001.jpg
frame_0002.jpg
...
frame_0150.jpg
```

the next video will continue with:

```text
frame_0151.jpg
frame_0152.jpg
...
```

This ensures that the frames generated during the same execution maintain unique numbering and prevents files from one video from overwriting those generated from another.

![Processed files](assets/images/finish_file.jpg)

---

### 7. Processing information

While the videos are being processed, the console displays information about the current operation.

![Start of the processing](assets/images/start_script.jpg)

For each video, the programme retrieves information such as:

- FPS.
- Total number of frames in the video.
- Duration.
- Number of frames extracted.

This information provides an overview of the video's basic characteristics and the results obtained during the extraction process.

---

### 8. Processing report

Once all selected videos have been processed, the programme automatically generates a `.txt` report containing a summary of the operation.

![Processing completed](assets/images/finish_script.jpg)

The report includes:

- Extraction interval used.
- Video file name.
- FPS.
- Total number of frames in the video.
- Video duration.
- Number of frames extracted from the video.
- Total number of videos processed.
- Total number of frames extracted.
- Destination folder.

---

## 📂 Output structure

After processing, the selected folder will have a structure similar to the following:

```text
Selected folder/
│
├── frames/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   ├── frame_0003.jpg
│   ├── frame_0004.jpg
│   ├── ...
│   └── frame_XXXX.jpg
│
└── reporte_frames_YYYYMMDD_HHMMSS.txt
```

The extracted frames are stored inside the `frames` folder.

The processing report is saved directly in the selected destination folder.

---

## 📊 Processing report

The generated report uses the following naming format:

```text
reporte_frames_YYYYMMDD_HHMMSS.txt
```

For example:

```text
reporte_frames_20260824_112030.txt
```

A typical report has a structure similar to the following:

```text
=================================================================
                    PROCESSING RESULTS
=================================================================

Extraction interval: 2.00 seconds

-----------------------------------------------------------------
Video 1
-----------------------------------------------------------------

File: example.mp4
FPS: 60.77
Frames: 18231
Duration: 300.02 seconds
Frames extracted: 151

=================================================================
SUMMARY
=================================================================

Videos processed: 1
Total frames extracted: 151

=================================================================
SAVE LOCATION
=================================================================

C:\Videos\frames
```

In this report, **“Frames”** refers to the total number of frames contained in the original video, while **“Frames extracted”** refers to the number of images generated by the programme according to the configured extraction interval.

---

## 🧠 Use in computer vision projects

One of the intended uses of this tool is preparing data for computer vision projects.

For example, a road pothole detection project could use the following workflow:

```text
🎥 Road video
        │
        ▼
Video Frame Extractor
        │
        ▼
🖼️ Extracted frames
        │
        ▼
🔎 Image selection
        │
        ▼
🏷️ Image labelling
        │
        ▼
📊 Dataset
        │
        ▼
🤖 Computer vision model
```

In a pothole detection project, the extracted frames can be manually reviewed to identify useful images containing potholes. These images can then be labelled and incorporated into a dataset for training a computer vision model.

The tool itself **does not perform pothole detection or image labelling**.

---

## ⚙️ Requirements

The project was **tested with Python 3.13.13**.

The following are required:

- Python 3.13 or a compatible version.
- OpenCV.
- Tkinter.

### Python version

The version used during development and testing was:

```text
Python 3.13.13
```

> Compatibility with other Python versions has not been tested extensively and may depend on the versions of the installed libraries.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/TuxidoMask/video_frame_extractor.git
cd video_frame_extractor
```

### 2. Install OpenCV

Install the main external dependency for the project:

```bash
pip install opencv-python
```

Tkinter is normally included with Python installations on Windows.

Depending on the operating system and Python distribution being used, it may be necessary to install Tkinter separately.

---

## ▶️ Usage

Run the Python script from the project directory:

```bash
python script.py
```

> Replace `script.py` with the actual name of the Python file if it is different.

The programme will guide you through the process using graphical windows.

---

## 🔢 Frame numbering

Frames are numbered consecutively using the following format:

```text
frame_0001.jpg
frame_0002.jpg
frame_0003.jpg
...
```

The numbering uses four digits and starts at `0001`.

During a single execution, the numbering continues across all selected videos. Therefore, frames generated by one video do not reuse the numbers assigned to frames from previously processed videos.

---

## ⚠️ Compatibility and limitations

- The minimum extraction interval is `0.5 seconds`.
- Frames are currently saved only in `.jpg` format.
- Video processing depends on OpenCV.
- Actual compatibility may vary depending on the video codec and encoding.
- Having a supported file extension does not guarantee that the video can be opened successfully.
- Large or long-duration videos may require a considerable amount of storage space.
- The extracted frame may not correspond exactly to the expected timestamp depending on the video's encoding and structure.
- The project was tested with Python `3.13.13`, but other Python versions have not been tested extensively.
- The tool is intended as an auxiliary utility rather than a complete video analysis system.

If OpenCV cannot open one of the selected videos, the programme displays an error message and continues with the next video.

---

## 🔮 Possible future improvements

Possible improvements for future versions include:

- Better compatibility with different video codecs.
- Improved extraction performance.
- Support for additional image formats.
- Image quality configuration.
- More detailed processing reports.
- A more complete graphical interface.
- Additional options for organising extracted frames.
- Optional inclusion of metadata associated with the frames.
- Improved error handling.

---

## 📁 Project structure

The project currently uses a simple structure:

```text
video_frame_extractor/
│
├── assets/
│   └── images/
│       ├── select_video.jpg
│       ├── select_file.jpg
│       ├── select_time_seconds.jpg
│       ├── name_file.jpg
│       ├── new_file.jpg
│       ├── result_frames.jpg
│       ├── finish_file.jpg
│       ├── start_script.jpg
│       └── finish_script.jpg
│
├── script.py
│
├── README.md
├── README.es.md
│
└── ...
```

The `images` folder contains the screenshots used in this README.

---

## 📄 Licence

This project currently does not include a specific licence.

If the project is to be distributed or reused publicly, adding an appropriate open-source licence is recommended.