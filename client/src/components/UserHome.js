import React, {useEffect, useState} from 'react'
import "./App.css";



const UserHome = ({ id, onDeleteSong }) => {
  const [songs, setSongs] = useState([]);

  //const { id } = song

  useEffect(() => {
    const testDeployedApt = async () => {
      let apiResults = await fetch("/songs")
        .then((r) => r.json())
        .then((data) => data);
      //console.table(apiResults)
      setSongs(apiResults);
    };
    testDeployedApt();
  }, []);

  //handles delete
  function handleDelete() {
    
    fetch(`/songs${id}`, {
      method: "DELETE",
    })
      .then((r) => r.json())
      .then(() => onDeleteSong(id));
  }

  return (
    <>
      <h1>My Home Page</h1>
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

export default UserHome;
