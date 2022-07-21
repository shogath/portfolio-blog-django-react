import React from 'react'
import { useEffect, useState } from 'react';
import axiosInstance from '../utils/axiosInstanse';
import { Link } from 'react-router-dom';

const PopularPosts = () => {

    const [popularPosts, setPopularPosts] = useState([])

    useEffect(() => {
        const controller = new AbortController();
        const getPopularPosts = async () => {
            try {
                let response = await axiosInstance.get('/blog/api/popular-posts/', {
                    signal: controller.signal,
                })
                setPopularPosts(response.data)
            } catch (err) {
                // console.log('There was a problem or request was cancelled.')
            }
        }
        getPopularPosts()
        return () => controller.abort()
    }, [])


    return (
        <div className="w3-col l4">
            <div className="w3-card w3-margin">
                <div className="w3-container w3-padding">
                    <h4>Popular Posts</h4>
                </div>
                <ul className="w3-ul w3-hoverable w3-white">
                    {popularPosts?.map((post, index) => (
                        <Link key={index} to={`/blog/${post?.slug}/`} style={{ textDecoration: 'none' }} onClick={() => window.scrollTo(0, 0)}>
                            <li className="w3-padding-16">
                                <img src={post?.thumbnail} alt={post?.title} className="w3-left w3-margin-right" style={{ width: 50 + "px" }} />
                                <span className="w3-large">{post?.title}</span><br />
                                <span className="w3-opacity">{post?.date}</span>
                            </li>
                        </Link>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default PopularPosts;

