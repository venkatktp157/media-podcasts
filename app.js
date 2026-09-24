document.addEventListener("DOMContentLoaded", async () => {
  try {
    const response = await fetch("media.json");
    const mediaItems = await response.json();

    const audioSelect = document.getElementById("audio-select");
    const videoSelect = document.getElementById("video-select");
    const audioContainer = document.getElementById("audio-container");
    const videoContainer = document.getElementById("video-container");

    const audioFiles = mediaItems.filter(item => item.type === "audio");
    const videoFiles = mediaItems.filter(item => item.type === "video");

    // Populate Audio Dropdown
    audioFiles.forEach(item => {
      const opt = document.createElement("option");
      opt.value = item.filename;
      opt.textContent = item.title;
      audioSelect.appendChild(opt);
    });

    // Populate Video Dropdown
    videoFiles.forEach(item => {
      const opt = document.createElement("option");
      opt.value = item.filename;
      opt.textContent = item.title;
      videoSelect.appendChild(opt);
    });

    // Handle Audio Selection
    audioSelect.addEventListener("change", (e) => {
      audioContainer.innerHTML = e.target.value
        ? `<audio controls src="${e.target.value}"></audio>`
        : "";
    });

    // Handle Video Selection
    videoSelect.addEventListener("change", (e) => {
      videoContainer.innerHTML = e.target.value
        ? `<video controls src="${e.target.value}"></video>`
        : "";
    });
  } catch (error) {
    console.error("Error loading media catalog:", error);
  }
});