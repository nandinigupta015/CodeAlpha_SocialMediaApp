function getCookie(name) {
  let cookieValue = null;

  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();

      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}

const csrftoken = getCookie("csrftoken");

// ✅ Run after page loads
document.addEventListener("DOMContentLoaded", () => {
  // ✅ Image Preview
  const imageUpload = document.getElementById("imageUpload");
  const preview = document.getElementById("imagePreview");

  if (imageUpload && preview) {
    imageUpload.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (ev) => {
        preview.src = ev.target.result;
        preview.classList.add("show");
      };
      reader.readAsDataURL(file);
    });
  }

  // ✅ Like Buttons AJAX
  const likeButtons = document.querySelectorAll(".like-btn");

  likeButtons.forEach((btn) => {
    // ✅ Apply liked look initially
    if (btn.dataset.liked === "true") {
      btn.classList.add("liked");
    }

    btn.addEventListener("click", async () => {
      const postId = btn.dataset.postId;

      const res = await fetch(`/like/${postId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
        },
      });

      const data = await res.json();

      const countSpan = document.getElementById(`like-count-${postId}`);
      if (countSpan) countSpan.innerText = data.like_count;

      if (data.liked) {
        btn.classList.add("liked");
        btn.dataset.liked = "true";
      } else {
        btn.classList.remove("liked");
        btn.dataset.liked = "false";
      }
    });
  });
});

// ✅ Add Comment AJAX
async function addComment(postId) {
  const input = document.getElementById(`comment-input-${postId}`);
  if (!input) return;

  const text = input.value.trim();
  if (!text) return;

  const res = await fetch(`/comment/${postId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrftoken,
    },
    body: `text=${encodeURIComponent(text)}`,
  });

  const data = await res.json();

  if (data.success) {
    input.value = "";

    // ✅ Update comment count
    const countSpan = document.getElementById(`comment-count-${postId}`);
    if (countSpan) {
      countSpan.innerText = data.comment_count;
    }

    // ✅ Add comment instantly in UI
    const commentsBox = document.getElementById(`comments-${postId}`);

    if (commentsBox) {
      const newComment = document.createElement("div");
      newComment.classList.add("comment");

      newComment.innerHTML = `
        <div class="comment-author">@${data.comment.username}</div>
        <div class="comment-text">${data.comment.text}</div>
      `;

      commentsBox.prepend(newComment);
    }
  }
}

