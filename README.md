# ✍️ YouTube Video Blog Content Creator

This project is a **content creation pipeline** that uses **YouTube videos** as input to generate comprehensive blog content. It leverages **CrewAI agents**, **YouTube Channel Search tools**, and **GPT-based models** to streamline blog research and writing processes.

---

## 🌟 Project Highlights

- **YouTube Video Research**: Extracts detailed information from targeted YouTube channels. 📊
- **Blog Content Writing**: Generates blog content with engaging narratives based on video data. ✍️
- **Customizable Tools**: Easily configure tools for different YouTube channels or content topics. ⚙️

---

🔍 **How It Works**

Step 1: Research Task

  - Agent: blog_researcher

      - Extracts relevant video content from a specified YouTube channel.
      - Summarizes the content into a detailed 3-paragraph report.

  - Tools: YoutubeChannelSearchTool
    
      - Searches for videos based on the specified topic within the YouTube channel.
        
Step 2: Writing Task

  - Agent: blog_writer
      - Processes research outputs and transforms them into engaging blog content.
      - Summarizes video data into narratives that are easy to read and informative.
      - Output: Saves the blog content as deepmind-blog-post.md.
        
Step 3: Execution

  - Research: Initializes blog_researcher with:
      - Role: Blog creator from YouTube videos.
      - Goal: Extract and analyze video content.
      - Write: Initializes blog_writer with:
      - Role: Blog writer.
      - Goal: Write detailed blogs based on video summaries.
