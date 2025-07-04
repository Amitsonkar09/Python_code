// JavaScript code to fetch and display GitHub user information and repositories
const userDetailsDiv = document.getElementById('user-details');
const repoList = document.getElementById('repo-list');

async function fetchGitHubUser(username) {
    const response = await fetch(`https://api.github.com/users/${username}`);
    const userData = await response.json();
    displayUserInfo(userData);
    fetchUserRepos(username);
}

function displayUserInfo(user) {
    userDetailsDiv.innerHTML = `
        <p><strong>Name:</strong> ${user.name}</p>
        <p><strong>Bio:</strong> ${user.bio}</p>
        <p><strong>Followers:</strong> ${user.followers}</p>
        <p><strong>Following:</strong> ${user.following}</p>
        <p><strong>Public Repos:</strong> ${user.public_repos}</p>
    `;
}

async function fetchUserRepos(username) {
    const response = await fetch(`https://api.github.com/users/${username}/repos`);
    const repos = await response.json();
    displayRepos(repos);
}

function displayRepos(repos) {
    repoList.innerHTML = repos.map(repo => `
        <li>
            <a href="${repo.html_url}" target="_blank">${repo.name}</a>
        </li>
    `).join('');
}

// Fetch GitHub user data for a specific username
fetchGitHubUser('octocat'); // Replace 'octocat' with any GitHub username
