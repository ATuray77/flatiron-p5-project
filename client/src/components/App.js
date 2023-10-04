import { Route, Switch } from "react-router-dom";
import "./App.css"
import NavBar from './NavBar';
import Home from "./Home";
import UserHome from "./UserHome";
import Login from "./Login";
import SignUp from "./SignUp";
import SongsPage from './SongsPage';
import SongForm from './SongForm';
import React, { useEffect, useState } from "react";
//import { Link } from "react-router-dom";

//ORIGINAL SONGS AND SETSONG STATES. NOW USING USER AND SETUSER FOR THE LOGIN PAGE
// function App() {
//   const [songs, setSongs] = useState([]);

  function App() {
    const [user, setUser] = useState(null);
    const [songs, setSongs] = useState([]);
    useEffect(() => {
      // auto-login
      fetch("/check_session").then((r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
    }, []);



  function handleOnFormSubmitted(addedSong) {
    const updatedSongs = [...songs, addedSong];
    setSongs(updatedSongs);
  }

  //handles delete
  function handleDeleteSong(id) {
    const updatedSongs = songs.filter((song) => song.id !== id);
    setSongs(updatedSongs);
  }

// THIS FUNCTION DID THE ORIGINAL FETCH. MODIFYING THIS TO ONLY ACCOMODATE THE SIGNUP OR LOGIN PAGE
//THIS WILL HAVE TO BE MOVED TO A NEW PAGE AFTER THE USER IS LOGGED IN
  useEffect(() => {
    fetch("https://new-json-server.onrender.com/songs")
    //fetch("http://localhost:3000/songs")
      .then((r) => r.json())
      .then((songs) => setSongs(songs));
  }, []);

  if (!songs) return <h2>Loading...</h2>;

  return (
    <>
    <NavBar user={user} setUser={setUser}/> 
    <div>
      {user ? (
      <Switch>
        <Route path="/songs">
          {/* <UserHome user={user}/> */}
          <SongsPage songs={songs} setSongs={setSongs} />
        </Route>
        <Route path="/form">
          <SongForm onFormSubmitted={handleOnFormSubmitted} />
        </Route>
        <Route exact path="/">
          <UserHome songs={songs} id={songs.id} onDeleteSong={handleDeleteSong} />
        </Route>
      </Switch>
      ) : (
      <Switch>
        <Route path="/signup">
          <SignUp setUser={setUser} />
        </Route>

        <Route path="/login">
          <Login setUser={setUser}/>
        </Route>

        <Route path="/">
          <Home />
        </Route>
      </Switch>
      )}
      
    </div>
    </>
  );
}

export default App;
