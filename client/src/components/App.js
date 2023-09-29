import { Route, Switch } from "react-router-dom";
import "./App.css"
import NavBar from './NavBar';
import Home from "./Home";
import SongsPage from './SongsPage';
import SongForm from './SongForm';
import React, { useEffect, useState } from "react";
//import { Link } from "react-router-dom";

function App() {
  const [songs, setSongs] = useState([]);

  //to handle delete
  //const { id } = songs

  function handleOnFormSubmitted(addedSong) {
    const updatedSongs = [...songs, addedSong];
    setSongs(updatedSongs);
  }

  //handles delete
  function handleDeleteSong(id) {
    const updatedSongs = songs.filter((song) => song.id !== id);
    setSongs(updatedSongs);
  }

  //if shits hit the fan we resolve back to this
  // function handleOnFormSubmitted(addedSong) {
  //   setSongs([...songs, addedSong]);
  // }

  useEffect(() => {
    fetch("https://new-json-server.onrender.com/songs")
    //fetch("http://localhost:3000/songs")
      .then((r) => r.json())
      .then((songs) => setSongs(songs));
  }, []);

  if (!songs) return <h2>Loading...</h2>;

  return (
    <div>
      <NavBar />
      <Switch>
        <Route path="/songs">
          <SongsPage songs={songs} setSongs={setSongs} />
        </Route>
        <Route path="/form">
          <SongForm onFormSubmitted={handleOnFormSubmitted} />
        </Route>
        <Route exact path="/">
          <Home songs={songs} id={songs.id} onDeleteSong={handleDeleteSong} />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
