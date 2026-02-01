import API from '../../baseURL/baseURL.jsx';
import React, { useState, useEffect } from 'react';
import BlogCard from './blogcard.jsx';
function BlogDetails(){
const [blog,setBlog]=useState([]);
useEffect(()=>{
 const fetchBlogs=async()=>{
    try{
      const response=await API.get('/blogs/');
      setBlog(response.data);
      console.log(response.data);
    }
    catch(err){
      console.log(`error: ${err.message}`);
    }
 }
 fetchBlogs();
},[]);
return(
<BlogCard items={blog}/>
);
}
export default BlogDetails;