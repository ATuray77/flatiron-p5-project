import React, {useEffect, useState} from 'react'
import "./App.css";



const Home = ({ id, onDeleteSong }) => {
  const [songs, setSongs] = useState([]);

  //const { id } = song

  useEffect(() => {
    const testDeployedApt = async () => {
      let apiResults = await fetch("https://new-json-server.onrender.com/songs")
        .then((r) => r.json())
        .then((data) => data);
      //console.table(apiResults)
      setSongs(apiResults);
    };
    testDeployedApt();
  }, []);

  //handles delete
  function handleDelete() {
    //fetch(`${process.env.REACT_APP_API_URL}/songs${id}`,{
    fetch(`https://new-json-server.onrender.com/songs${id}`, {
      method: "DELETE",
    })
      .then((r) => r.json())
      .then(() => onDeleteSong(id));
  }

  return (
    <>
      <h1>Home Page</h1>
      {songs.map((song) => (
        <li key={song.id}>
          {song.Title}
          <button onClick={handleDelete} id={song.id}>
            Delete
          </button>
        </li>
      ))}
    </>
  );
};

export default Home;
