//import React from 'react'
import { Link } from 'react-router-dom'
//import "./App.css";
import React, { useState } from "react";
//import Home from './Home';


function SongsList({ songs, setSongs }) {
  const [searchTerm, setSearchTerm] = useState("");

  const onFormSubmission = (e) => {
    e.preventDefault();

    setSongs(songs.filter((song) => song.Title.toLowerCase().includes(searchTerm)));
    // const filteredSongs = songs.filter(song =>
    //   song.Title.toLowerCase().includes(searchTerm))
  };

  const renderSongs = Object.keys(songs).map((songID) => (
    <li key={songID}>
      <Link to={`/songs/${songID}`}>{songs[songID].Title}</Link>
    </li>
  ));

 // const songPassToHome = songs.map((song) => <Home song={song} />);

  return (
    <div>
      <form onSubmit={onFormSubmission}>
        <label>
          🔎
          <input type="search" value={searchTerm} placeholder="search..." onChange={(e) => setSearchTerm(e.target.value.toLowerCase())} />
        </label>
      </form>
      <ol>{renderSongs}</ol>
    </div>
  );
}

export default SongsList