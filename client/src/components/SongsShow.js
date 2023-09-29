import React from 'react'
import { useParams } from 'react-router-dom'

function SongsShow({ songs }) {
  console.log(songs)

  const params = useParams(); //this function pulls out the id params
  console.log(params)
  

  return (
    <div>
      <h3>Title: {songs[params.songID].Title}</h3>
      <h4>Artist: {songs[params.songID].Artist}</h4>
      <h5>Style: {songs[params.songID].Style}</h5>
      <h5>Lyrics: {songs[params.songID].Lyrics}</h5>
      <p>{songs[params.songID].Lyrics}</p>
    </div>
  );
}

export default SongsShow