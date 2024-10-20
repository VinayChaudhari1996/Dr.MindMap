# Dr.MindMap - Medical Knowledge Visualization Tool
![image](https://github.com/user-attachments/assets/ca241d08-4abd-44b9-900e-3e50718918d5)


Demo : https://drmindmap.streamlit.app/

## Overview
Dr.MindMap is an interactive Streamlit application that generates comprehensive medical mind maps using Google's Generative AI (Gemini Pro). It helps healthcare professionals, students, and medical researchers visualize detailed information about diseases, their symptoms, treatments, and related medical knowledge in an organized, hierarchical format.

## 🌟 Key Features
- 🏥 Specialized medical knowledge visualization
- 🤖 AI-powered content generation using Gemini Pro
- 📊 Interactive mind map visualization
- 📝 Detailed markdown output
- 🔒 Secure API handling
- 📱 Responsive interface
- 💊 Comprehensive medical information structure

## 🎯 Target Audience
- Medical Professionals
- Healthcare Students
- Medical Researchers
- Healthcare Educators
- Clinical Staff
- Medical Content Creators

## 📋 Medical Information Structure
The application generates structured information including:
- Disease Definition
- Causes
- Types
- Clinical Features
- Symptoms
- Prevention
- Diagnosis
- Useful Medicines

## 🛠️ Technical Requirements

### Prerequisites
- Python 3.7+
- Google API key (Gemini Pro access)
- Internet connection

### Dependencies
```
streamlit
streamlit-markmap
google.generativeai
```

## 📦 Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Get Google API Access:
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Generate an API key for Gemini Pro

2. API Key Setup Options:
   - Enter directly in application sidebar
   - Set as environment variable:
     ```bash
     export GOOGLE_API_KEY='your-api-key'
     ```

## 🚀 Usage

1. Launch the application:
```bash
streamlit run app.py
```

2. Access via web browser (default: http://localhost:8501)

3. In the sidebar:
   - Enter your Google API key
   - Input the medical condition or disease
   - Click "Submit"

4. View Results:
   - Interactive mind map visualization
   - Detailed markdown text output

## 🏗️ Application Structure

### Interface Components:
1. **Sidebar**
   - Application title "Dr.MindMap"
   - API key input field
   - Topic input area
   - Submit button

2. **Main Content Area**
   - Mind map visualization
   - Markdown text display

### Core Functions:

#### `main()`
- Initializes application
- Manages UI components
- Handles session state

#### `create_markdown(input_data)`
- Generates medical content using AI
- Parameters:
  - `input_data`: Medical topic/condition
- Returns:
  - Structured markdown content
- Implements medical knowledge template

## 📊 Output Format

### Markdown Structure:
```markdown
# Disease Name

## Definition
- Detailed explanation
- Key characteristics

## Causes
- Primary causes
- Risk factors

## Types
- Classifications
- Variants

## Clinical Features
- Physical signs
- Observable characteristics

## Symptoms
- Patient experiences
- Warning signs

## Prevention
- Preventive measures
- Lifestyle modifications

## Diagnosis
- Diagnostic methods
- Tests required

## Useful Medicines
- Treatment options
- Medications
```

## ⚠️ Important Notes

### Medical Disclaimer
This tool is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

### Data Accuracy
- AI-generated content should be verified by medical professionals
- Always cross-reference with current medical literature
- Keep up with latest medical guidelines

## 🔒 Security Considerations
- Secure API key handling
- No medical data storage
- Private session management

## 🐛 Troubleshooting

Common Issues:
1. **API Key Problems**
   - Verify key validity
   - Check API activation status
   - Confirm Gemini Pro access

2. **Visualization Issues**
   - Clear browser cache
   - Check internet connection
   - Refresh application

## 🔄 Updates and Maintenance
- Regular content template updates
- Medical information structure revisions
- Performance optimizations

## 👥 Contributing
Contributions welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License
[Specify your license here]

## 🙏 Acknowledgments
- Streamlit development team
- Markmap visualization library
- Google Generative AI team
- Medical professionals who provided feedback

## 📞 Support
For technical issues or suggestions:
- Open an issue on GitHub

## 🔄 Version History
- 1.0.0: Initial release
