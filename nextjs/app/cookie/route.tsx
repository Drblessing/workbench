'use server';

import { type NextRequest } from 'next/server';
import { cookies } from 'next/headers';

export async function GET(request: NextRequest) {
  const url = new URL(request.url);
  const token_value = url.searchParams.get('token');

  if (token_value) {
    cookies().set('token', token_value);
    return new Response(`Hello, ${token_value}!`);
  }

  const token = cookies().get('token');

  if (token) {
    return new Response(`Hello, ${token.value}!`);
  }

  return new Response('Hello, stranger!');
}
