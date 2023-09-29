//import "./App.css";
import "./Form.css";
//import { useRef } from "react";


function SongForm({ onFormSubmitted }) {

  const onSubmit = (e) => {
    e.preventDefault();
    const formData = Object.fromEntries(new FormData(e.target));
    console.log(formData);

    fetch("http://localhost:3000/songs", {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((r) => r.json())
      .then((addedSong) => onFormSubmitted(addedSong));
  };

  return (
      <form onSubmit={onSubmit} className="form">
        <label>
          Title
          <input type="text" name="Title" />
        </label>
        <label>
          Artist
          <input type="text" name="Artist" />
        </label>
        <label>
          Style
          <select name="Style">
            <option>praise</option>
            <option>Worship</option>
          </select>
        </label>
        <label>
          Lyrics
          <textarea name="Lyrics"></textarea>
        </label>
        <button type="submit">Add a song</button>
      </form>
  );
}

export default SongForm;
